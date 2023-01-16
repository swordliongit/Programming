from scapy_route import host_finder, host_writer, host_analyzer, ip_retriever
from utility import create_directory
from interface_operation import modem_login_init, interface_operation_modify_compare
from http_request import odoo_login, send_datato_odoo, fetch_datafrom_odoo
import threading
from queue import Queue
#import PySimpleGUI as sg
import tkinter

needed_hosts = {}
compare_queue = Queue()

def network_scan(output, target_ip, fhfile="./hosts/found_hosts.json", mhfile="./hosts/modem_hosts.json"):
    
    mac_filter = ""
    
    # information retrieval - pre operation phase
    import os
    if os.stat("./support/info.txt").st_size != 0:
        with open("./support/info.txt") as file:
            #target_ip = file.readline().split('=')[1].strip('\n')   # ip range to scan
            mac_filter = file.readline().split('=')[1].strip('\n')  # mac filter to fetch
    else:
        with open("./support/info.txt", 'w') as file:
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
            
def modem_read_and_odoo_post(output, x_hotel_name, network_scan_caller_button, modem_configure_caller_button):
    
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
    output.insert(tkinter.END, "Modem analizi basladi. Bu islem zaman alabilir, lutfen bekleyin..\n")
    output.config(state='disabled')
    
    mode = "read"
    
    threads = []
    
    read_queue = Queue()
    global compare_queue

    for ip, mac in zip(ip_list, mac_list): # call multiple versions of the function simultaneously
        t = threading.Thread(target=modem_login_init, args=(ip, mac, mode, x_hotel_name, read_queue, compare_queue, ""))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    """
    READ OPERATION END
    """
    #########################

    ############################
    """
    ODOO POST START
    """ 
    
    odoo_login()
    
    modem_read_result_list = {"modems":[]}
    
    while not read_queue.empty():
        modem_read_result_list["modems"].append(read_queue.get())
        
    send_datato_odoo(modem_read_result_list)

    output.config(state='normal')
    output.insert(tkinter.END, "Veriler Odoo'ya gonderildi!..\n")
    output.config(state='disabled')
    """
    ODOO POST END
    """
    ############################

    # import tkinterthread
    # tkinterthread.call_nosync(confirmation)
    network_scan_caller_button.config(state="normal")
    modem_configure_caller_button.config(state="normal")
    
    output.config(state='normal')
    output.insert(tkinter.END, "Veriler Odoo'ya gönderildi, degisiklik yaptiginiz ayarlari uygulamak icin\n'Web Ayarlarini Uygula Butonuna' basin. Tekrar ag taramasi yapmak icin\n'Ag Taramasi' butonuna basin.\n" + "-"*15 + "\n")
    output.config(state='disabled')
    # while not event_scan_or_fetch.is_set():
    #     pass
    
    # event_scan_or_fetch.clear()

    
def modem_configure(output, network_scan_caller_button, modem_read_and_odoo_post_caller_button, modem_configure_caller_button):   
    
    """
    FETCH START
    """
    output.config(state='normal')
    output.insert(tkinter.END, "Odoo'dan veri toplaniyor..\n")
    output.config(state='disabled')
    odoo_login()
    fetched_modem_list: list = fetch_datafrom_odoo()
    
    ips_of_modified_modems = []
    sorted_fetched_modem_list = []
    
    sorted_fetched_modem_list = sorted(fetched_modem_list, key=lambda x: x['x_ip'])
    
    modem_mapping = {modem['x_mac']: modem['x_ip'] for modem in sorted_fetched_modem_list}
    
    global needed_hosts
    
    ips_of_modified_modems = [host['ip'] for host in needed_hosts if host['mac'] in modem_mapping]
    
    """
    FETCH END
    """    
    
    
    """
    MODIFY OPERATION START
    """
    output.config(state='normal')
    output.insert(tkinter.END, "Modem konfigurasyonu basladi. Bu islem zaman alabilir, lutfen bekleyin..\n")
    output.config(state='disabled')
    
    mode = "modify"
    
    threads = []
    
    fields_to_compare_list = []
    
    global compare_queue

    while not compare_queue.empty():
        fields_to_compare_list.append(compare_queue.get()) 
        
    for modem in fields_to_compare_list:
        if not modem['x_ip'] in ips_of_modified_modems:
            fields_to_compare_list.remove(modem)
        
    sorted_fields_to_compare_list = sorted(fields_to_compare_list, key=lambda x: x['x_ip'])
    
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
    output.insert(tkinter.END, "Modem konfigurasyonu bitti..\n")
    output.config(state='disabled')
    
    """
    MODIFY OPERATION END
    """
    #######################
    output.config(state='normal')
    output.insert(tkinter.END, "Verileri Odoo'ya göndermek için 'Sonuclari Odoo'ya Gonder' butonuna basin.\n" + "-"*15 + "\n")
    output.config(state='disabled')
    
    modem_read_and_odoo_post_caller_button.config(state="normal")
    network_scan_caller_button.config(state="normal")
    modem_configure_caller_button.config(state="disable")
    
        