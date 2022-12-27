import requests
import json

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

url = 'http://localhost:8069/web/dataset/call_kw/res.partner/create'
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
    "Content-Type": "application/json",
    "Cookie": cookie
    }
myobj = {"id":33,"jsonrpc":"2.0","method":"call","params":{"args":[{"partner_gid":0,"additional_info":False,"image_1920":False,"__last_update":False,"is_company":False,"active":True,"company_type":"person","name":"proto5","parent_id":False,"company_name":False,"type":"contact","street":False,"street2":False,"city":False,"state_id":False,"zip":False,"country_id":False,"vat":False,
                                                                    "x_uptime":"5h 32m 12s",
                                                                    "x_wireless_status":"enable",
                                                                    "x_channel":"auto",
                                                                    "x_mac":"1c:18:4a:47:63:80",
                                                                    "x_ip":"192.168.5.1",
                                                                    "x_subnet":"255.255.255.0",
                                                                    "x_dhcp":False,
                                                                    "x_ssid":False,
                                                                    "x_enable_wireless":True,
                                                                    "x_enable_ssid":True,
                                                                    "x_manual_time":False,
                                                                    "x_new_password":False,
                                                                    "x_wan_status":False,
                                                                    "x_lan_info":False,
                                                                    
                                                                    "phone":False,"mobile":False,"user_ids":[],"email":False,"message_follower_ids":[],"activity_ids":[],"message_ids":[]}],"model":"res.partner","method":"create","kwargs":{"context":{"lang":"tr_TR","tz":"Europe/Istanbul","uid":2,"allowed_company_ids":[1],"params":{"id":11,"cids":1,"menu_id":96,"action":122,"model":"res.partner","view_type":"form"},"default_is_company":True}}}}
    
x = requests.post(url, json = myobj, headers=headers)
#print the response text (the content of the requested file):
#return str(x.content)
#response = x.json()
#return str(response['jsonrpc'])
#aşağıdaki işlemle önce json parse edildi sonra 0-52 ye kadar substring yapıldı
last_result = json.loads((x.content))
print(str(last_result))

