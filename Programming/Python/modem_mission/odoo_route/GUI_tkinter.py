import tkinter
from tkinter import ttk
from threading import Thread, Event
from main import operator_main, network_scan


event_scan_or_fetch = Event()   

first_press = True

def modem_configure(modem_read_and_odoo_post_button): 
    
    global event_scan_or_fetch
    event_scan_or_fetch.set()
    
    network_scan_button.config(state="disable")
    modem_configure_button.config(state="disable")
    modem_read_and_odoo_post_button.config(state="disable")

def networkscan_scapy(target_ip, output):
    # modem_configure_button.config(state="disable")
    modem_read_and_odoo_post_button.config(state="disable")
    
    global event_scan_or_fetch
    global first_press
    
    if first_press:
        first_press = False
    else:
        first_press = True
        event_scan_or_fetch.set()
    
    network_scan_button.config(state="disable")
    
    thread = Thread(target=network_scan, args=(target_ip, output))
    thread.start()
    output.update()
    
    #enable other 2 buttons after 5 seconds
    root.after(5000, lambda: modem_read_and_odoo_post_button.config(state="enable"))
    root.after(5000, lambda: network_scan_button.config(state="enable"))
    # network_scan(target_ip, output)

def modem_read_and_odoo_post(output, x_hotel_name, target_ip, modem_read_and_odoo_post_button):
    
    network_scan_button.config(state="disable")
    modem_configure_button.config(state="disable")
    modem_read_and_odoo_post_button.config(state="disable")
        
    
    thread = Thread(target=operator_main, args=(output, x_hotel_name, event_scan_or_fetch, network_scan_button, modem_read_and_odoo_post_button, modem_configure_button))
    thread.start()
    output.update()
    
def GUI_init():
    pass


    
    

root = tkinter.Tk()
root.title("Modem Configuration Program")

# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure(2, weight=1)
# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(2, weight=1)

hotel_label = ttk.Label(root, text="Otel Adi Girin ------>")
hotel_label.grid(row=0, column=0, padx=10, pady=10)

hotel_name_input = ttk.Entry(root)
hotel_name_input.grid(row=0, column=1, padx=10, pady=10)

ip_label = ttk.Label(root, text="IP Menzilini Girin ------>")
ip_label.grid(row=1, column=0, padx=10, pady=10)

ip_input = ttk.Entry(root)
ip_input.grid(row=1, column=1, padx=10, pady=10)

network_scan_button = ttk.Button(root, text="Simdi Ag Taramasi Yap", command=lambda: networkscan_scapy(ip_input.get(), output))
network_scan_button.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

modem_read_and_odoo_post_button = ttk.Button(root, text="Sonuclari Odoo'ya gonder", command=lambda: modem_read_and_odoo_post(output, hotel_name_input.get(), ip_input.get(), modem_read_and_odoo_post_button))
modem_read_and_odoo_post_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

modem_configure_button = ttk.Button(root, text="Web Ayarlarini Uygula", command=lambda: modem_configure(modem_read_and_odoo_post_button))
modem_configure_button.grid(row=2, column=2, padx=10, pady=10)

output = tkinter.Text(root)
output.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

modem_configure_button.config(state="disable")
modem_read_and_odoo_post_button.config(state="disable")

root.mainloop()

# root.after(0, GUI_init)