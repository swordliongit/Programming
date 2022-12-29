from scapy_route import host_finder, host_writer, host_analyzer, ip_retriever
from utility import create_directory
from modem_login import modem_login_init, modem_login
from http_request import odoo_login, send_datato_odoo
from interface_operation import login_controller
import threading

from time import sleep
def main():
    
    fhfile: str = "hosts/found_hosts.json" # found hosts file
    mhfile: str = "hosts/modem_hosts.json" # modem hosts file   
    
    # information retrieval - pre operation phase
    import os
    if os.stat("info.txt").st_size != 0:
        with open("info.txt") as file:
            target_ip = file.readline().split('=')[1].strip('\n')   # ip range to scan
            mac_filter = file.readline().split('=')[1].strip('\n')  # mac filter to fetch
    else:
        with open("info.txt", 'w') as file:
            file.writelines("target=192.168.5.0/24")
            file.writelines("mac_filter=1c:18:4a")

    # start of main operation
    ########################
    
    create_directory("./hosts/") #create our directory for our host files

    hosts: list = host_finder(target_ip ) # network scan

    host_writer(fhfile, hosts ) # write found hosts into fhfile

    needed_hosts: dict = host_analyzer(fhfile, mhfile, mac_filter) # filter found hosts based on 1c:18:4a mac and return a list of them
    
    if not needed_hosts:
        print("No modems found!")
        return
    
    # host operation finished
    ########################
    

    driver = modem_login_init() #initialize the chrome driver

    ip_list = []
    for ip in ip_retriever(needed_hosts): # yield ips of the filtered hosts one by one
        ip_list.append(ip)


    ########################
    # First read operation start

    threads1 = []
    threads2 = []

    mode = "read"

    for ip in ip_list: # call multiple versions of the function simultaneously
        t1 = threading.Thread(target=modem_login, args=(driver, ip))
        t2 = threading.Thread(target=login_controller, args=(driver, mode))
        threads1.append(t1)
        threads2.append(t2)
        t1.start()
        t2.start()
        
    for t1, t2 in zip(threads1, threads2): # wait for all threads to finish
        t1.join()
        t2.join()

    sleep(1.5)
    # First read operation end
    #########################
    
    
    
    ##########################
    # Modify operation start
    
    mode = "modify"
    
    
    login_controller(driver, mode, ip_for_dhcp=ip)
    
    sleep(1.5)
    
    # Modify operation end
    #######################
    
    
    
    ########################
    # Second read operation start
    from queue import Queue
    queue = Queue()
    
    mode = "read"
    
    threads1.clear()
    threads2.clear()

    for ip in ip_list: # call multiple versions of the function simultaneously
        t1 = threading.Thread(target=modem_login, args=(driver, ip))
        t2 = threading.Thread(target=login_controller, args=(driver, mode, "", queue))
        threads1.append(t1)
        threads2.append(t2)
        t1.start()
        t2.start()
        
    for t1, t2 in zip(threads1, threads2): # wait for all threads to finish
        t1.join()
        t2.join()
      
    # Second read operation end  
    ########################
    
    # Modem data retrieved, time to send it to Odoo 
    print("Logging in Odoo..")
    odoo_login()
    print("Sending data to Odoo..")
    #print(queue.qsize())
    result: dict = queue.get() # result is obj_dict
    
    send_datato_odoo(result)
        
    print("Data sent!..")
    
    #########################

if __name__ == "__main__":
    main()