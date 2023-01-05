from scapy_route import host_finder, host_writer, host_analyzer, ip_retriever
from utility import create_directory
from interface_operation import modem_login_init, interface_operation_modify_compare
from http_request import odoo_login, send_datato_odoo, fetch_datafrom_odoo
import threading

from time import sleep

def network_scan(target_ip, fhfile, mhfile, mac_filter):
    hosts: list = host_finder(target_ip) # network scan

    host_writer(fhfile, hosts ) # write found hosts into fhfile

    needed_hosts: dict = host_analyzer(fhfile, mhfile, mac_filter) # filter found hosts based on 1c:18:4a mac and return a list of them
    
    if not needed_hosts:
        print("No modems found!")
        return
    
    return needed_hosts

    
def main(x_hotel_name):
    
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

    create_directory("./hosts/") # create our directory for our host files
    
    
    
    while True:

        needed_hosts = network_scan(target_ip, fhfile, mhfile, mac_filter)
        
        #driver = modem_login_init() #initialize the chrome driver

        ip_list = []
        for ip in ip_retriever(needed_hosts): # yield ips of the filtered hosts one by one
            ip_list.append(ip)


        ########################
        # Read operation start

        
        
        #lock = threading.Lock()
        
        mode = "read"
        
        threads = []
        
        from queue import Queue
        
        read_queue = Queue()
        compare_queue = Queue()

        for ip in ip_list: # call multiple versions of the function simultaneously
            t = threading.Thread(target=modem_login_init, args=(ip, mode, x_hotel_name, read_queue, compare_queue, None, False))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # Read operation end
        #########################

        ############################
        # Modem data retrieved, time to send it to Odoo 
        
        print("Logging in Odoo for send..")
        
        odoo_login()
        print("Sending data to Odoo..")  
        while not read_queue.empty():
            result = read_queue.get()
            send_datato_odoo(result)
    
        print("Data sent!..")
        
        ############################
        
        input("Press enter to start fetching if you have done modifying..")
        
        ############################
        # Time to get all the changed modems' data from Odoo
        print("Logging in Odoo for fetch..")
        odoo_login()
        print("Fetching data from Odoo..")
        fetched_modem_list: list = fetch_datafrom_odoo()
        
        sorted_fetched_modem_list = sorted(fetched_modem_list, key=lambda x: x['x_ip'])
        
        ############################
        
        ##########################
        # Modify operation start
        
        mode = "modify"
        
        threads.clear()

        
        fields_to_compare_list = []

        while not compare_queue.empty():
            fields_to_compare_list.append(compare_queue.get()) 
            
        
        sorted_fields_to_compare_list = sorted(fields_to_compare_list, key=lambda x: x['x_ip'])
        
        #print(sorted_fetched_modem_list)
        #print(sorted_fields_to_compare_list)
        #input()
        
        fields_to_change_list = []
        
        for fields_to_change in interface_operation_modify_compare(sorted_fetched_modem_list, sorted_fields_to_compare_list):
            fields_to_change_list.append(fields_to_change)
        
        
        for modem, fields_to_change in zip(sorted_fetched_modem_list, fields_to_change_list):
            ip = modem['x_ip']
            t = threading.Thread(target=modem_login_init, args=(ip, mode, "", None, None, fields_to_change, False))
            threads.append(t)
            t.start()
          
            
        for t in threads:# wait for all threads to finish
            t.join()

        input("Press enter to loop again")
        
        # Modify operation end
        #######################
        

if __name__ == "__main__":
    main()