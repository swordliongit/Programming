from scapy_route import host_finder, host_writer, host_analyzer, ip_retriever
from utility import create_directory
from interface_operation import modem_login_init, interface_operation_modify_compare
from http_request import odoo_login, send_datato_odoo, fetch_datafrom_odoo
import threading

from time import sleep

def network_scan(target_ip, fhfile, mhfile, mac_filter):
    
    target_ip = target_ip + "/24"
    
    hosts: list[dict[str, str]] = host_finder(target_ip) # network scan

    host_writer(fhfile, hosts ) # write found hosts into fhfile

    needed_hosts: dict = host_analyzer(fhfile, mhfile, mac_filter) # filter found hosts based on 1c:18:4a mac and return a list of them
    
    if not needed_hosts:
        print("No modems found!")
        return
    
    return needed_hosts

    
def main(output_queue, x_hotel_name, target_ip):
    
    fhfile: str = "hosts/found_hosts.json" # found hosts file
    mhfile: str = "hosts/modem_hosts.json" # modem hosts file   
    
    mac_filter = ""
    
    # information retrieval - pre operation phase
    import os
    if os.stat("info.txt").st_size != 0:
        with open("info.txt") as file:
            #target_ip = file.readline().split('=')[1].strip('\n')   # ip range to scan
            mac_filter = file.readline().split('=')[1].strip('\n')  # mac filter to fetch
    else:
        with open("info.txt", 'w') as file:
            #file.writelines("target=192.168.5.0/24")
            file.writeline("mac_filter=1c:18:4a")

    create_directory("./hosts/") # create our directory for our host files
    
    
    # Program main loop start
    while True:

        needed_hosts = network_scan(target_ip, fhfile, mhfile, mac_filter)
        
        # mac is needed in case reading from modem's web interface has mac : 00:00:00:00:00:00
        # so it won't read it and instead, it'll get the real mac from the network scan, to send to Odoo

        ip_list = []
        
        mac_list = []
        
        for ip, mac in ip_retriever(needed_hosts): # yield ips of the filtered hosts one by one
            ip_list.append(ip)
            mac_list.append(mac)


        ########################
        """
        READ OPERATION START
        """
        mode = "read"
        
        threads = []
        
        from queue import Queue
        
        read_queue = Queue()
        compare_queue = Queue()

        for ip, mac in zip(ip_list, mac_list): # call multiple versions of the function simultaneously
            t = threading.Thread(target=modem_login_init, args=(ip, mac, mode, x_hotel_name, read_queue, compare_queue, ""))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
            
        #output.print("Operation done")
        #output_queue.put("Operation done")

        """
        READ OPERATION END
        """
        #########################

        ############################
        """
        ODOO SEND START
        """ 
        
        print("Logging in Odoo for send..")
        
        odoo_login()
        print("Sending data to Odoo..")  
        
        modem_read_result_list = {"modems":[]}
        
        while not read_queue.empty():
            modem_read_result_list["modems"].append(read_queue.get())
            
        send_datato_odoo(modem_read_result_list)
    
        print("Data sent!..")
        
        """
        ODOO SEND END
        """
        ############################
        """
        FETCH CONFIRMATION START
        """
        
        import GUI
        
        # event = threading.Event()
        # event.clear()
        # #output_queue.put("fetch_confirmation")
        # thread = threading.Thread(target=GUI.fetch_confirmation, args=(event,))
        # thread.start()
        # event.wait()
        
        input("...................")
        
        """
        FETCH CONFIRMATION END
        """
        ############################
        """
        FETCH START
        """
        # Time to get all the changed modems' data from Odoo
        print("Logging in Odoo for fetch..")
        odoo_login()
        print("Fetching data from Odoo..")
        fetched_modem_list: list = fetch_datafrom_odoo()
        
        sorted_fetched_modem_list = sorted(fetched_modem_list, key=lambda x: x['x_ip'])
        
        ips_of_modified_modems = []
        
        modem_mapping = {modem['x_mac']: modem['x_ip'] for modem in sorted_fetched_modem_list}
        
        ips_of_modified_modems = [host['ip'] for host in needed_hosts if host['mac'] in modem_mapping]
        
        """
        FETCH END
        """    
        
        
        
        ############################
        
        ##########################
        """
        MODIFY OPERATION START
        """
        
        mode = "modify"
        
        threads.clear()
        
        fields_to_compare_list = []

        while not compare_queue.empty():
            fields_to_compare_list.append(compare_queue.get()) 
            
        for modem in fields_to_compare_list:
            if not modem['x_ip'] in ips_of_modified_modems:
                fields_to_compare_list.remove(modem)
            
        sorted_fields_to_compare_list = sorted(fields_to_compare_list, key=lambda x: x['x_ip'])
        
        #print(sorted_fetched_modem_list)
        #print(sorted_fields_to_compare_list)
        #input()
        
        fields_to_change_list = []
        
        for fields_to_change in interface_operation_modify_compare(sorted_fetched_modem_list, sorted_fields_to_compare_list):
            fields_to_change_list.append(fields_to_change)
        
        
        for ip, fields_to_change in zip(ips_of_modified_modems, fields_to_change_list):
            t = threading.Thread(target=modem_login_init, args=(ip, "", mode, "", None, None, fields_to_change))
            threads.append(t)
            t.start()
          
            
        for t in threads:# wait for all threads to finish
            t.join()

        #input("Press enter to loop again")
        
        """
        MODIFY OPERATION END
        """
        #######################
        
        sleep(2)
        

if __name__ == "__main__":
    pass