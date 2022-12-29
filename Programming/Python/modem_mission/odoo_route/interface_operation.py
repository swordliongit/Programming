from selenium_dependencies import *
from queue import Queue
from time import sleep
import modem_login

field_dict = {}

x_wireless_status = "disable"

def login_controller(driver, mode, ip_for_dhcp="", queue=Queue()):
    
    modem_list = [{'x_enable_wireless':True, 'x_enable_ssid2':False, 'x_enable_ssid3':False, 'x_manual_time':"2023-04-23 16:39:55", 'x_dhcp':False}]
    
    global field_dict
    if mode == "read":
        field_dict = interface_operation_read(driver, queue)
    elif mode == "modify":
        for fields_to_change in interface_operation_modify_compare(modem_list, field_dict):
            interface_operation_modify(driver, fields_to_change, ip_for_dhcp)

def interface_operation_read(driver, queue):
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
    
    obj_dict =  {"id":43,"jsonrpc":"2.0","method":"call","params":{
        "args":[
            {"partner_gid":0,"additional_info":False,"image_1920":False,"__last_update":False,"is_company":False,"active":True,"company_type":"person","name":"protomodem","parent_id":False,"company_name":False,"type":"contact","street":False,"street2":False,"city":False,"state_id":False,"zip":False,"country_id":False,"vat":False,         
                #we need to add into this dictionary e.g. "x_ip":"192.168.5.1", ...
             "phone":False,"mobile":False,"user_ids":[],"email":False,"message_follower_ids":[],"activity_ids":[],"message_ids":[]
             }
            ],
        "model":"res.partner","method":"create","kwargs":{"context":{"lang":"tr_TR","tz":"Europe/Istanbul","uid":2,"allowed_company_ids":[1],"params":{"cids":1,"menu_id":96,"action":122,"model":"res.partner","view_type":"kanban"},"default_is_company":True}}}}
    
    # XXX START OF THE AUTOMATION XXX
    
    # Network -> Uptime
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Status"))).click()
    
    sleep(0.5)
    
    x_uptime = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "uptime"))).text
    field_dict['x_uptime'] = x_uptime
    
    
    # LAN Information -> Wireless Status & Channel & MAC & IP, device info
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "LAN Information"))).click()
    
    sleep(0.5)
    
    global x_wireless_status
    
    x_wireless_status = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wlan-ifc-status"))).text
    field_dict['x_wireless_status'] = x_wireless_status
    
    # channel may or may not be present, depending on wireless status(on/off)
    if x_wireless_status == "enable":
        x_channel = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "wlan-ifc-channel")))
        field_dict['x_channel'] = x_channel.text
    else:
        field_dict['x_channel'] = "-"

        
    x_mac = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ra0-ifc-mac"))).text
    field_dict['x_mac'] = x_mac
    
    x_device_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#maincontent > div > div:nth-child(4) > div > div:nth-child(3) > table"))).text
    field_dict['x_device_info'] = x_device_info
    
    # Network: LAN Settings -> IP, Subnet, dhcp
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "LAN Settings"))).click()
    
    sleep(0.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.ipaddr')))
    x_ip = field.get_attribute('value')
    field_dict['x_ip'] = x_ip
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.netmask')))
    x_subnet = field.get_attribute('value')
    field_dict['x_subnet'] = x_subnet
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.dhcp\.dnsmasq_0\.dhcp_en")))
    x_dhcp = True if field.is_selected() else False
    field_dict['x_dhcp'] = x_dhcp
    
    # Network: WLAN -> Enable Wireless
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "WLAN"))).click()
    
    sleep(1.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.wifi_ctrl_0\.enabled")))
    x_enable_wireless = True if field.is_selected() else False
    field_dict['x_enable_wireless'] = x_enable_wireless
    
    if x_enable_wireless:
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra0\.enabled")))
        x_enable_ssid1 = True if field.is_selected() else False
        field_dict['x_enable_ssid1'] = x_enable_ssid1
        
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra1\.enabled")))
        x_enable_ssid2 = True if field.is_selected() else False
        field_dict['x_enable_ssid2'] = x_enable_ssid2
        
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra2\.enabled")))
        x_enable_ssid3 = True if field.is_selected() else False
        field_dict['x_enable_ssid3'] = x_enable_ssid3
        
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra3\.enabled")))
        x_enable_ssid4 = True if field.is_selected() else False
        field_dict['x_enable_ssid4'] = x_enable_ssid4
    else:
        field_dict['x_enable_ssid1'] = False
        field_dict['x_enable_ssid2'] = False
        field_dict['x_enable_ssid3'] = False
        field_dict['x_enable_ssid4'] = False
        
    # Network: Time Synchronisation -> Manual Time
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Time Synchronisation"))).click()
    
    sleep(0.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.ntpclient\.cfg04887d\.manual_time')))
    x_manual_time = field.get_attribute('value')
    field_dict['x_manual_time'] = x_manual_time
    
    # System: Administration -> New Password
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "System"))).click()
    
    sleep(0.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pw1')))
    x_new_password = field.get_attribute('value')
    field_dict['x_new_password'] = x_new_password
    
    ############################# XXX
    print("Read Operation Completed..")
    ############################# XXX
    
    # XXX END OF THE AUTOMATION XXX
        
    for k, v in field_dict.items():
        obj_dict['params']['args'][0].update({k:v}) # add newly fetched fields into the main dict
    
    queue.put(obj_dict) 
    
    return field_dict
        
    """try:
        
        
        # go to another page
        driver.find_element(By.LINK_TEXT, "Time Synchronisation").click()

        # find the text field
        txt_field = driver.find_element(By.ID, "cbid.ntpclient.cfg04887d.manual_time")
        txt_field.click()
        txt_field.send_keys(Keys.CONTROL + "a") # select all
        txt_field.send_keys(Keys.DELETE) 
        txt_field.send_keys("2016-04-23 12:00:39") # change

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "cbi.apply"))).click() # Apply button
    except Exception as ex:
        print("Exception Occured. Operation failed...")
        print(type(ex))
        print(ex)"""
    
def interface_operation_modify_compare(modem_list: list, field_dict: dict):
    
    # modem_list = [{'x_ip': "192.168.5.1", ...}, {'x_ip: "192.168.5.2", ...}, ...]

    print("Comparing values..")
    for modem in modem_list: # modem = {'x_ip': "192.168.5.1", ...}
        fields_to_change = {}
        for k, v in modem.items(): # k = 'x_ip' v = "192.168.5.1"
            if v != field_dict[k]: # field_dict['x_ip']
                fields_to_change[k] = v # if a field is modified, add it into our dict
        yield fields_to_change # modify for each modem   
    
def interface_operation_modify(driver, fields_to_change: dict, ip):
    print("Modify Operation launched..")
    for k, v in fields_to_change.items():
        match k:
            case 'x_uptime':
                pass
            case 'x_wireless_status':
                pass
            case 'x_channel':
                pass
            case 'x_mac':
                pass
            case 'x_device_info':
                pass
            case 'x_ip':
                modify_x_ip(driver, v)
            case 'x_subnet':
                modify_x_subnet(driver, v)
            case 'x_dhcp':
                modify_x_dhcp(driver, v, ip)
            case 'x_enable_wireless':
                modify_x_enable_wireless(driver, v)
            case 'x_enable_ssid1':
                modify_x_enable_ssid1(driver, v)
            case 'x_enable_ssid2':
                modify_x_enable_ssid2(driver, v)
            case 'x_enable_ssid3':
                modify_x_enable_ssid3(driver, v)
            case 'x_enable_ssid4':
                modify_x_enable_ssid4(driver, v)
            case 'x_manual_time':
                modify_x_manual_time(driver, v)
            case 'x_new_password':
                modify_x_new_password(driver, v)
    print("Modify operation completed..")

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
    
def modify_x_dhcp(driver, v, ip):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "LAN Settings"))).click()
    sleep(0.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cbid\.dhcp\.dnsmasq_0\.dhcp_en')))
    field.click()
    
    # Apply button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
    
    WebDriverWait(driver, 10).until(lambda d: Alert(d)).accept()
    sleep(15)
    
    modem_login.modem_login(driver, ip)
    sleep(0.5)
    
    
def modify_x_enable_wireless(driver, v):
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "WLAN"))).click()
    sleep(1.5)
    
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.wifi_ctrl_0\.enabled")))
    field.click()
    
    # Apply button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
    sleep(10)
    
def modify_x_enable_ssid1(driver, v):
    global x_wireless_status
    if x_wireless_status == "enable":
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "WLAN"))).click()
        sleep(1.5)
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra0\.enabled")))
        field.click()
        
        # Apply button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
        sleep(10)
    else: pass       
def modify_x_enable_ssid2(driver, v):
    global x_wireless_status
    if x_wireless_status == "enable":
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "WLAN"))).click()
        sleep(1.5)
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra1\.enabled")))
        field.click()
        
        # Apply button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
        sleep(10)
    else: pass
def modify_x_enable_ssid3(driver, v):
    global x_wireless_status
    if x_wireless_status == "enable":
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "WLAN"))).click()
        sleep(1.5)
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra2\.enabled")))
        field.click()
        
        # Apply button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
        sleep(10)
    else: pass
def modify_x_enable_ssid4(driver, v):
    global x_wireless_status
    if x_wireless_status == "enable":
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Network"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "WLAN"))).click()
        sleep(1.5)
        field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cbid\.wireless\.ra3\.enabled")))
        field.click()
        
        # Apply button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#maincontent > form > div.cbi-section > div > div > input:nth-child(1)"))).click()
        sleep(10)
    else: pass
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