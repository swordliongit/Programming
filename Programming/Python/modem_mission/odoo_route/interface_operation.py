from selenium_dependencies import *
from queue import Queue
from time import sleep
from modem_login import modem_login, modem_logout

default_fields_dict = {}

x_wireless_status = "disable"

def operation_controller(driver, mode: str, fetched_modem_list: list, x_hotel_name: str, ip_for_dhcp="", queue=None):
     
    global default_fields_dict
    if mode == "read":
        default_fields_dict = interface_operation_read(driver, x_hotel_name, queue)
    elif mode == "modify":
        for fields_to_change in interface_operation_modify_compare(fetched_modem_list, default_fields_dict):
            interface_operation_modify(driver, fields_to_change, ip_for_dhcp)
        
def interface_operation_read(driver, x_hotel_name, queue):
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
    
    global default_fields_dict
    
    x_uptime = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "uptime"))).text
    default_fields_dict['x_uptime'] = x_uptime
    
    
    # LAN Information -> Wireless Status & Channel & MAC & IP, device info
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "LAN Information"))).click()
    
    sleep(0.5)
    
    global x_wireless_status
    
    
    x_wireless_status = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wlan-ifc-status"))).text
    default_fields_dict['x_wireless_status'] = x_wireless_status
    
    # channel may or may not be present, depending on wireless status(on/off)
    if x_wireless_status == "enable":
        x_channel = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "wlan-ifc-channel")))
        default_fields_dict['x_channel'] = x_channel.text
    else:
        default_fields_dict['x_channel'] = "-"

        
    x_mac = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ra0-ifc-mac"))).text
    default_fields_dict['x_mac'] = x_mac
    
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
    
    queue.put(obj_dict) 
    
    return default_fields_dict
       
def interface_operation_modify_compare(fetched_modem_list: list, default_fields_dict: dict):
    
    # fetched_modem_list = [{'x_ip': "192.168.5.1", ...}, {'x_ip: "192.168.5.2", ...}, ...]

    print("Comparing values..")
    
    fields_we_want = ['x_ip', 'x_subnet', 'x_dhcp', 'x_enable_wireless', 'x_enable_ssid1', 
                      'x_enable_ssid2', 'x_enable_ssid3', 'x_enable_ssid4', 'x_manual_time',
                      'x_new_password']
    for modem in fetched_modem_list: # modem = {'x_ip': "192.168.5.1", ...}
        
        filtered_modem = {key: modem[key] for key in fields_we_want}
        fields_to_change = {}
        
        # we need to put x_dhcp to the end of the dict of fields that need to be modified, 
        # to avoid long wait times that cause problems
        is_x_dhcp_present = False
        
        for k, v in filtered_modem.items(): # e.g. k = 'x_ip' v = "192.168.5.1"
            if v != default_fields_dict[k]: # if "192.168.5.1" != default_fields_dict['x_ip']
                fields_to_change[k] = v # if a field is modified, add it into our dict
                if k == 'x_dhcp':
                    x_dhcp_temp = fields_to_change.pop('x_dhcp') # x_dhcp present, take it out
                    is_x_dhcp_present = True
        if is_x_dhcp_present:
            fields_to_change['x_dhcp'] = x_dhcp_temp     # put it back to the end of the dict
        yield fields_to_change # modify for each modem   
    
def interface_operation_modify(driver, fields_to_change: dict, ip_for_dhcp):
    print("Modify Operation launched..")
    
    x_enable_wireless_routine = []
    
    for k, v in fields_to_change.items():
        match k:
            case 'x_ip':
                modify_x_ip(driver, v)
            case 'x_subnet':
                modify_x_subnet(driver, v)
            case 'x_dhcp':
                modify_x_dhcp(driver, ip_for_dhcp)
            case 'x_enable_wireless':
                x_enable_wireless_routine.append(k)
            case 'x_enable_ssid1':
                x_enable_wireless_routine.append(k)
            case 'x_enable_ssid2':
                x_enable_wireless_routine.append(k)
            case 'x_enable_ssid3':
                x_enable_wireless_routine.append(k)
            case 'x_enable_ssid4':
                x_enable_wireless_routine.append(k)
            case 'x_manual_time':
                modify_x_manual_time(driver, v)
            case 'x_new_password':
                modify_x_new_password(driver, v)
                
    modify_x_enable_wireless(driver, x_enable_wireless_routine)
    print("Modify operation completed..")
    
    #modem_logout(driver)
    
def modify_x_ip(driver, v):
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "LAN Settings"))).click()
    sleep(0.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.ipaddr')))
    field.clear()
    field.send_keys(v)
    
def modify_x_subnet(driver, v):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "LAN Settings"))).click()
    sleep(0.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.netmask')))
    field.clear()
    field.send_keys(v)
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
    sleep(1)
    
def modify_x_dhcp(driver, ip):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "LAN Settings"))).click()
    sleep(0.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.dhcp_en')))
    field.click()
    
    # Apply button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
    
    WebDriverWait(driver, 10).until(lambda d: Alert(d)).accept()
    sleep(50)
    
    modem_login(driver, ip, dhcp_mode=True)
    sleep(0.5)
    
def modify_x_enable_wireless(driver, x_enable_wireless_routine):
    
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "WLAN"))).click()
    sleep(1.5)
    
    for field in x_enable_wireless_routine:
        match field:
            case 'x_enable_wireless':  
                
                field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.wifi_ctrl_0\.enabled")))
                
                if not field.is_selected():
                    field.click()
                    break
            case 'x_enable_ssid1':
                modify_x_enable_ssid1(driver)
            case 'x_enable_ssid2':
                modify_x_enable_ssid2(driver)
            case 'x_enable_ssid3':
                modify_x_enable_ssid3(driver)
            case 'x_enable_ssid4':
                modify_x_enable_ssid4(driver)
    # Apply button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
    sleep(10)
    
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
    
def modify_x_manual_time(driver, v):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Time Synchronisation"))).click()
    sleep(0.5)
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.ntpclient\.cfg04887d\.manual_time')))
    field.clear()
    field.send_keys(v)
    
    # Apply button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
    sleep(1)
    
def modify_x_new_password(driver, v):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "System"))).click()
    sleep(0.5)
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pw1')))
    field.click()
    field.send_keys(v)