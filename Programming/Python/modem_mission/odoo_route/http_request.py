import requests
import json


def odoo_login():
    url = 'http://localhost:8069/web/session/authenticate'
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        "Content-Type": "application/json"
        }
    myobj = {
        "jsonrpc": "2.0",
        "params": {
            "login": "kilicarslan.business@gmail.com",
            "password": "0987612345",
            "db": "modem"
        }
    }
    x = requests.post(url, json = myobj, headers=headers)
    #print the response text (the content of the requested file):
    #return str(x.content)
    #response = x.json()
    #return str(response['jsonrpc'])
    #aşağıdaki işlemle önce json parse edildi sonra 0-52 ye kadar substring yapıldı
    global cookie
    cookie = ((x.headers)['Set-Cookie'])[0:51]

    print(cookie)

########################

def send_datato_odoo(modem_data):
    url = 'http://localhost:8069/web/dataset/call_kw/res.partner/create'
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        "Content-Type": "application/json",
        "Cookie": cookie
        }
    myobj = modem_data 
    
    
    """{"id":43,"jsonrpc":"2.0","method":"call","params":{
        "args":[
            {"partner_gid":0,"additional_info":False,"image_1920":False,"__last_update":False,"is_company":False,"active":True,"company_type":"person","name":"proto5","parent_id":False,"company_name":False,"type":"contact","street":False,"street2":False,"city":False,"state_id":False,"zip":False,"country_id":False,"vat":False,"x_uptime":False,"x_wireless_status":False,"x_channel":False,"x_mac":False,"x_ip":False,"x_device_info":False,"x_subnet":False,"x_dhcp":False,"x_enable_wireless":False,"x_enable_ssid1":False,"x_enable_ssid2":False,"x_enable_ssid3":False,"x_enable_ssid4":False,"x_manual_time":False,"x_new_password":False,"x_wan_status":False,"x_lan_info":False,"phone":False,"mobile":False,"user_ids":[],"email":False,"message_follower_ids":[],"activity_ids":[],"message_ids":[]
             
             }
            ],
        "model":"res.partner","method":"create","kwargs":{"context":{"lang":"tr_TR","tz":"Europe/Istanbul","uid":2,"allowed_company_ids":[1],"params":{"cids":1,"menu_id":96,"action":122,"model":"res.partner","view_type":"kanban"},"default_is_company":True}}}}"""
    
    
        
    x = requests.post(url, json = myobj, headers=headers)
    #print the response text (the content of the requested file):
    #return str(x.content)
    #response = x.json()
    #return str(response['jsonrpc'])
    #aşağıdaki işlemle önce json parse edildi sonra 0-52 ye kadar substring yapıldı
    last_result = json.loads((x.content))
    print(str(last_result))

