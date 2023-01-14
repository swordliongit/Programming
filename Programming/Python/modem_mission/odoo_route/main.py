from scapy_route import host_finder, host_writer, host_analyzer, ip_retriever
from utility import create_directory
from interface_operation import modem_login_init, interface_operation_modify_compare
from http_request import odoo_login, send_datato_odoo, fetch_datafrom_odoo
import threading

#import PySimpleGUI as sg

from time import sleep

import tkinter

needed_hosts = {}

def network_scan(target_ip, output, fhfile="hosts/found_hosts.json", mhfile="hosts/modem_hosts.json"):
    
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
    
    global needed_hosts
    
    target_ip = target_ip + "/24"
    
    hosts: list[dict[str, str]] = host_finder(target_ip, output) # network scan

    host_writer(fhfile, hosts, output) # write found hosts into fhfile

    needed_hosts = host_analyzer(fhfile, mhfile, mac_filter) # filter found hosts based on 1c:18:4a mac and return a list of them
    
    if not needed_hosts:
        print("No modems found!")
        return
    
    return needed_hosts

def confirmation():
    from tkinter import messagebox

    fetch_warning = messagebox.askokcancel("Devam etmek icin modemleri kurgulayin, kurgulama bittiyse OK'a basin.")
    if fetch_warning:
        continue_execution = messagebox.askyesno("Degistirilen ayarlari uygulamak icin devam etmek istiyor musunuz?")
        if not continue_execution:
            exit()
    
    # fetch_warning = sg.PopupNoTitlebar('Devam etmek icin modemleri kurgulayin, kurgulama bittiyse OK\'a basin.', button_type=sg.POPUP_BUTTONS_OK, grab_anywhere=True)
    # if fetch_warning == "OK":
    #     # check if user wants to continue
    #     continue_execution = sg.popup_yes_no('Degistirilen ayarlari uygulamak icin devam etmek istiyor musunuz?', no_titlebar=True, grab_anywhere=True)
    #     if continue_execution == 'No':
    #         exit()
    
def operator_main(output, x_hotel_name, event_scan_or_fetch, network_scan_button, modem_read_and_odoo_post_button, modem_configure_button):
    
    # Program operator_main loop start
    # while True:
    # global needed_hosts
    # needed_hosts = network_scan(target_ip, output)
    
    # mac is needed in case reading from modem's web interface has mac : 00:00:00:00:00:00
    # so it won't read it and instead, it'll get the real mac from the network scan, to send to Odoo
    global needed_hosts
    
    ip_list = []
    
    mac_list = []
    
    for ip, mac in ip_retriever(needed_hosts): # yield ips of the filtered hosts one by one
        ip_list.append(ip)
        mac_list.append(mac)


    ########################
    """
    READ OPERATION START
    """
    output.config(state='normal')
    output.insert(tkinter.END, "Read operation launched..\n")
    output.config(state='disabled')
    
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

    output.config(state='normal')
    output.insert(tkinter.END, "Read operation completed!\n")
    output.config(state='disabled')
    
    """
    READ OPERATION END
    """
    #########################

    ############################
    """
    ODOO SEND START
    """ 
    output.config(state='normal')
    output.insert(tkinter.END, "Logging in Odoo for send..\n")
    output.config(state='disabled')
    
    odoo_login()
    
    output.config(state='normal')
    output.insert(tkinter.END, "Sending data to Odoo..\n")
    output.config(state='disabled')
    
    modem_read_result_list = {"modems":[]}
    
    while not read_queue.empty():
        modem_read_result_list["modems"].append(read_queue.get())
        
    send_datato_odoo(modem_read_result_list)

    output.config(state='normal')
    output.insert(tkinter.END, "Data sent!..\n")
    output.config(state='disabled')
    """
    ODOO SEND END
    """
    ############################
    """
    FETCH CONFIRMATION START
    """
    # import tkinterthread
    # tkinterthread.call_nosync(confirmation)
    network_scan_button.config(state="normal")
    modem_configure_button.config(state="normal")
    
    output.config(state='normal')
    output.insert(tkinter.END, "Tarama bitti ve sonuçlar Odoo'ya gönderildi, ayarlari uygulamak için 'Web Ayarlarini Uygula Butonuna' basin. veya 'Ag Taramasi' yapin.\n")
    output.config(state='disabled')
    while not event_scan_or_fetch.is_set():
        pass
    
    event_scan_or_fetch.clear()
    
    # tkinterthread.call(confirmation)

    
    # event_fetch = threading.event_fetch()
    # event_fetch.clear()
    # #output_queue.put("fetch_confirmation")
    # thread = threading.Thread(target=GUI.fetch_confirmation, args=(event_fetch,))
    # thread.start()
    # event_fetch.wait()
    
    """
    FETCH CONFIRMATION END
    """
    ############################
    """
    FETCH START
    """
    # Time to get all the changed modems' data from Odoo
    output.config(state='normal')
    output.insert(tkinter.END, "Logging in Odoo for fetch..\n")
    output.config(state='disabled')
    odoo_login()
    output.config(state='normal')
    output.insert(tkinter.END, "Fetching data from Odoo..\n")
    output.config(state='disabled')
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
    output.config(state='normal')
    output.insert(tkinter.END, "Modify operation started...\n")
    output.config(state='disabled')
    
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
    output.config(state='normal')
    output.insert(tkinter.END, "Modify operation completed..\n")
    output.config(state='disabled')
    
    """
    MODIFY OPERATION END
    """
    #######################
    output.config(state='normal')
    output.insert(tkinter.END, "Modem ayarlama tamamlandi..\n")
    output.config(state='disabled')
    
    modem_read_and_odoo_post_button.config(state="normal")
    modem_configure_button.config(state="disable")
    
        
if __name__ == "__operator_main__":
    pass