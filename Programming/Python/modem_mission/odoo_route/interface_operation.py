from selenium_dependencies import *
from queue import Queue
#from multiprocessing import Queue

from threading import Lock

from time import sleep
#from modem_login import modem_login, modem_logout

from collections import OrderedDict




def modem_login_init(ip, mac, mode, x_hotel_name, read_queue, compare_queue, fields_to_change):
    """function to set browser to run in background, initialize driver object

    Returns:
        Chrome driver: driver to return
    """
    
    from selenium.webdriver.chrome.options import Options

    #chrome_options = Options()
    #chrome_options.add_argument("--headless") # silent browser
    
    #driver = webdriver.Chrome("chromedriver", options=chrome_options)
    
    driver = webdriver.Chrome("chromedriver")
    
    if mode == "read":
        field_list_and_read_data = modem_login_control(driver, ip, mac, mode, x_hotel_name, None, ip_for_x_manual_time=ip)
    
        default_fields_dict = field_list_and_read_data[0]
    
        read_data = field_list_and_read_data[1]
    
        read_queue.put(read_data)
    
        compare_queue.put(default_fields_dict)
    elif mode == "modify":
        modem_login_control(driver, ip, mac, mode, None, fields_to_change, ip_for_x_manual_time=ip)
    
def is_logged_out(driver):
    try:
        driver.find_elements(By.ID, "login_in")
    except:
        return False
    else:
        return True

 
def modem_logout(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
    WebDriverWait(driver, 10).until(lambda d: Alert(d)).accept()
    sleep(0.5)  
 
def modem_login(driver, ip):
    url = "http://" + ip + "/cgi-bin/luci"
    
    username = ""
    password = ""
    
    import os
    if os.stat("modem_settings.txt").st_size != 0:
        with open("modem_settings.txt") as file:
            username = file.readline().split('=')[1].strip('\n')
            password = file.readline().split('=')[1]
    else:
        with open("modem_settings.txt", 'w') as file:
            file.writelines("username="+username)
            file.writelines("password="+password)
    
    try:
        print("Trying to log in...")

        driver.get(url) # open the url
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.ID, "login_in").click() # login button
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/form/div[3]/button[1]"))).click()

        #WebDriverWait(driver, 5).until(lambda driver: "http://192.168.1.1/cgi-bin/luci/admin/" != driver.current_url)
    except:
        ############################# XXX
        print("Login failed!")
        ############################# XXX
        return -1 # XXX GOTTA CHANGE
     
def modem_login_control(driver, ip, mac, mode, x_hotel_name, fields_to_change, ip_for_x_manual_time):
    """function to read username and password and open the login screen to log into the site
    
    """  
    modem_login(driver, ip)

    return operation_controller(driver, mode, x_hotel_name, fields_to_change, mac, ip_for_x_manual_time=ip_for_x_manual_time) 
    
    
    #current_url = driver.current_url



def operation_controller(driver, mode: str, x_hotel_name: str, fields_to_change, mac, ip_for_x_manual_time):
     
    # XXX global default_fields_dict XXX try this
     
    if mode == "read":
        #default_fields_dict = {}
        read_data = interface_operation_read(driver, x_hotel_name, mac)
        default_fields_dict = read_data[0]
        return default_fields_dict, read_data[1]
    elif mode == "modify":
        interface_operation_modify(driver, fields_to_change, ip_for_x_manual_time=ip_for_x_manual_time)
    return None
        
def interface_operation_read(driver, x_hotel_name, mac):
    """function that does the actual search operation inside the page and retrieves elements

    Args:
        driver (_type_): _description_
        output (_type_): GUI log screen output object to pass through
    """

    ############################# XXX
    print("Logged in successfully!")
    ############################# XXX

    ############################# XXX
    print("Read Operation launched..")
    ############################# XXX
    
    obj_dict =  {"id":63,"jsonrpc":"2.0","method":"call","params":{"args":[{"modem_image":False,"__last_update":False,"name":"protometa","x_uptime":False,"x_wireless_status":False,"x_channel":False,"x_mac":False,"x_device_info":False,"x_ip":False,"x_subnet":False,"x_dhcp":False,"x_enable_wireless":False,"x_enable_ssid1":False,"x_enable_ssid2":False,"x_enable_ssid3":False,"x_enable_ssid4":False,"x_manual_time":False,"x_new_password":False,"modem_id":False,"city":False,"live_status":"offline","last_action_user":3,"modem_status":False,"modem_home_mode":False,"customer_id":[[6,False,[]]],"modem_update":False,"modem_version":False}],"model":"modem.profile","method":"create","kwargs":{"context":{"lang":"en_US","tz":"Europe/Istanbul","uid":2,"allowed_company_ids":[1]}}}}
    
    # XXX START OF THE AUTOMATION XXX
    
    # Network -> Uptime
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Status"))).click()
    
    sleep(0.5)
    
    default_fields_dict = {}
    
    x_uptime = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "uptime"))).text
    default_fields_dict['x_uptime'] = x_uptime
    
    # LAN Information -> Wireless Status & Channel & MAC & IP, device info
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "LAN Information"))).click()
    
    sleep(0.5)
    
    x_wireless_status = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wlan-ifc-status"))).text
    default_fields_dict['x_wireless_status'] = x_wireless_status
    
    # channel may or may not be present, depending on wireless status(on/off)
    if x_wireless_status == "enable":
        x_channel = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "wlan-ifc-channel")))
        default_fields_dict['x_channel'] = x_channel.text
    else:
        default_fields_dict['x_channel'] = ""

    #x_mac = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ra0-ifc-mac"))).text
    
    #if x_mac == "00:00:00:00:00:00": # Fix the error on interface reading
    #    x_mac = mac
    default_fields_dict['x_mac'] = mac
    
    x_device_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#maincontent > div > div:nth-child(4) > div > div:nth-child(3) > table"))).text
    default_fields_dict['x_device_info'] = x_device_info
    
    # Network: LAN Settings -> IP, Subnet, dhcp
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "LAN Settings"))).click()
    
    sleep(0.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.ipaddr')))
    x_ip = field.get_attribute('value')
    default_fields_dict['x_ip'] = x_ip
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.netmask')))
    x_subnet = field.get_attribute('value')
    default_fields_dict['x_subnet'] = x_subnet
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.dhcp\.dnsmasq_0\.dhcp_en")))
    x_dhcp = True if field.is_selected() else False
    default_fields_dict['x_dhcp'] = x_dhcp
    
    # Network: WLAN -> Enable Wireless
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "WLAN"))).click()
    
    sleep(1.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.wifi_ctrl_0\.enabled")))
    x_enable_wireless = True if field.is_selected() else False
    default_fields_dict['x_enable_wireless'] = x_enable_wireless
    
    if x_enable_wireless:
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra0\.enabled")))
        x_enable_ssid1 = True if field.is_selected() else False
        default_fields_dict['x_enable_ssid1'] = x_enable_ssid1
        
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra1\.enabled")))
        x_enable_ssid2 = True if field.is_selected() else False
        default_fields_dict['x_enable_ssid2'] = x_enable_ssid2
        
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra2\.enabled")))
        x_enable_ssid3 = True if field.is_selected() else False
        default_fields_dict['x_enable_ssid3'] = x_enable_ssid3
        
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra3\.enabled")))
        x_enable_ssid4 = True if field.is_selected() else False
        default_fields_dict['x_enable_ssid4'] = x_enable_ssid4
    else:
        default_fields_dict['x_enable_ssid1'] = False
        default_fields_dict['x_enable_ssid2'] = False
        default_fields_dict['x_enable_ssid3'] = False
        default_fields_dict['x_enable_ssid4'] = False
        
    # Network: Time Synchronisation -> Manual Time
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Time Synchronisation"))).click()
    
    sleep(0.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.ntpclient\.cfg04887d\.manual_time')))
    x_manual_time = field.get_attribute('value')
    default_fields_dict['x_manual_time'] = x_manual_time
    
    # System: Administration -> New Password
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "System"))).click()
    
    sleep(0.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pw1')))
    x_new_password = field.get_attribute('value')
    default_fields_dict['x_new_password'] = x_new_password
    
    
    default_fields_dict['x_hotel_name'] = x_hotel_name
    
    import datetime
    
    default_fields_dict['x_update_date'] = str(datetime.datetime.now())
    
    ############################# XXX
    print("Read Operation Completed..")
    ############################# XXX
    
    modem_logout(driver)
    
    # XXX END OF THE AUTOMATION XXX
        
    for k, v in default_fields_dict.items():
        obj_dict['params']['args'][0].update({k:v}) # add newly fetched fields into the main dict
    
    print("\n")
    #queue.put(obj_dict) 
    
    #sleep(1)
    
    return default_fields_dict, obj_dict
       
def interface_operation_modify_compare(fetched_modem_list: list, fields_to_compare_list: list):
    
    # fetched_modem_list = [{'x_ip': "192.168.5.1", ...}, {'x_ip: "192.168.5.2", ...}, ...]

    print("Comparing values..")
    
    fields_we_want = ['x_ip', 'x_subnet', 'x_dhcp', 'x_enable_wireless', 'x_enable_ssid1', 
                      'x_enable_ssid2', 'x_enable_ssid3', 'x_enable_ssid4', 'x_manual_time',
                      'x_new_password']
    
    for modem, fields_to_compare in zip(fetched_modem_list, fields_to_compare_list): # modem = {'x_ip': "192.168.5.1", ...}
        filtered_modem = {key: modem[key] for key in fields_we_want}
        fields_to_change = OrderedDict()
        
        for k, v in filtered_modem.items(): # e.g. k = 'x_ip' v = "192.168.5.1"
            if v != fields_to_compare[k]: # if "192.168.5.1" != default_fields_dict['x_ip']
                fields_to_change[k] = v # if a field is modified, add it into our dict
        print(fields_to_change, "\n")
        
        if 'x_reboot' in modem and 'x_reboot' == True: #This is a button so I can't check the state of it in the read operation
            fields_to_change['x_reboot'] = modem['x_reboot']
            
        yield fields_to_change # modify for each modem
        
    if 'x_reboot' in fields_to_change and 'x_reboot' == True:
        fields_to_change.move_to_end('x_reboot', last=True)
        
    print("Values compared..")   
    
def interface_operation_modify(driver, fields_to_change: OrderedDict(), ip_for_x_manual_time):
    print("Modify Operation launched..")
    
    WLAN_task_list = []
    
    LAN_Settings_task_list = []
    
    for k, v in fields_to_change.items():
        
        match k:
            case 'x_ip':
                LAN_Settings_task_list.append({k:v})
            case 'x_subnet':
                LAN_Settings_task_list.append({k:v})
            case 'x_dhcp':
                LAN_Settings_task_list.append(k)
            case 'x_enable_wireless':
                WLAN_task_list.append(k)
                WLAN_task_list.append(v)
            case 'x_enable_ssid1':
                WLAN_task_list.append(k)
            case 'x_enable_ssid2':
                WLAN_task_list.append(k)
            case 'x_enable_ssid3':
                WLAN_task_list.append(k)
            case 'x_enable_ssid4':
                WLAN_task_list.append(k)
            case 'x_manual_time':
                modify_x_manual_time(driver, v, ip_for_x_manual_time=ip_for_x_manual_time)
            case 'x_new_password':
                modify_x_new_password(driver, v)
            case 'x_reboot':
                pass
                
    
    
    if len(WLAN_task_list) != 0:
        if 'x_enable_wireless' in WLAN_task_list:
            WLAN_task_list.remove('x_enable_wireless')
            WLAN_task_list.insert(0, 'x_enable_wireless')      
        modify_x_enable_wireless(driver, WLAN_task_list)
    
    if len(LAN_Settings_task_list) != 0:
        modify_WLAN_task_control(driver, LAN_Settings_task_list)
        
    if 'x_reboot' in fields_to_change:
        modify_x_reboot(driver)
    
    print("Modify operation completed..")
    
    if is_logged_out(driver):
        return
    else:
        modem_logout(driver)

def modify_x_reboot(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'System'))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Reboot'))).click()
    sleep(0.5)
    # reboot button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#maincontent > div > div:nth-child(2) > div > div > div:nth-child(3) > div > input'))).click()
    WebDriverWait(driver, 10).until(lambda d: Alert(d)).accept()
    sleep(60)

def modify_WLAN_task_control(driver, LAN_Settings_task_list):
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "LAN Settings"))).click()
    sleep(0.5)
    
    for field in LAN_Settings_task_list:
        if isinstance(field, dict):
            if 'x_ip' in field:
                modify_x_ip(driver, field['x_ip'])
            if 'x_subnet' in field:
                modify_x_subnet(driver, field['x_subnet'])
        if field == 'x_dhcp':
            modify_x_dhcp(driver)
                     
    # Apply button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
    
    WebDriverWait(driver, 10).until(lambda d: Alert(d)).accept()

    sleep(5)
    
def modify_x_ip(driver, v):
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.ipaddr')))
    field.clear()
    field.send_keys(v)
    
def modify_x_subnet(driver, v):
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.netmask')))
    field.clear()
    field.send_keys(v)
    
def modify_x_dhcp(driver):

    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.dhcp_en')))
    field.click()
    
def modify_x_enable_wireless(driver, WLAN_task_list):
    
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "WLAN"))).click()
    sleep(1.5)
    
    x_enable_wireless = True if True in WLAN_task_list else False
    
    for field in WLAN_task_list:
        match field:
            case 'x_enable_wireless':  
                field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.wifi_ctrl_0\.enabled")))
                field.click()
            case 'x_enable_ssid1':
                if x_enable_wireless:
                    modify_x_enable_ssid1(driver) 
            case 'x_enable_ssid2':
                if x_enable_wireless:
                    modify_x_enable_ssid2(driver)
            case 'x_enable_ssid3':
                if x_enable_wireless:
                    modify_x_enable_ssid3(driver)
            case 'x_enable_ssid4':
                if x_enable_wireless:
                    modify_x_enable_ssid4(driver)
    # Apply button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
    sleep(50)
    
def modify_x_enable_ssid1(driver):

    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra0\.enabled")))
    field.click()
       
def modify_x_enable_ssid2(driver):
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra1\.enabled")))
    field.click()
     
def modify_x_enable_ssid3(driver):
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra2\.enabled")))
    field.click()
    
def modify_x_enable_ssid4(driver):

    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra3\.enabled")))
    field.click()
    
def modify_x_manual_time(driver, v, ip_for_x_manual_time):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Time Synchronisation"))).click()
    sleep(0.5)
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.ntpclient\.cfg04887d\.manual_time')))
    field.clear()
    field.send_keys(v)
    
    # Apply button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
    sleep(5)
    
    if is_logged_out(driver):
        modem_login(driver, ip_for_x_manual_time)
    
def modify_x_new_password(driver, v):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "System"))).click()
    sleep(0.5)
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pw1')))
    field.click()
    field.send_keys(v)