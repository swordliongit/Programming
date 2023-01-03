from selenium_dependencies import *
from time import sleep
from queue import Queue
#from interface_operation import operation_controller

def modem_login_init(ip, mode, fetched_modem_list, x_hotel_name, dhcp_mode=False, queue=None):
    """function to set browser to run in background, initialize driver object

    Returns:
        Chrome driver: driver to return
    """
    
    from selenium.webdriver.chrome.options import Options

    #chrome_options = Options()
    #chrome_options.add_argument("--headless") # silent browser
    
    #driver = webdriver.Chrome("chromedriver", options=chrome_options)
    
    driver = webdriver.Chrome("chromedriver")
    
    #return driver
    
    modem_login(driver, ip, mode, fetched_modem_list, x_hotel_name, dhcp_mode, queue)
    
 
def modem_logout(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
    WebDriverWait(driver, 10).until(lambda d: Alert(d)).accept()
    sleep(0.5)  
     
def modem_login(driver, ip, mode, fetched_modem_list, x_hotel_name, dhcp_mode=False, queue=None):
    """function to read username and password and open the login screen to log into the site
    
    """  
    url = "http://" + ip + "/cgi-bin/luci"
    
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
        if dhcp_mode:
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.NAME, "password").send_keys(password)
            driver.find_element(By.ID, "login_in").click() # login button
        else:
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

    operation_controller(driver, mode, fetched_modem_list, x_hotel_name, ip_for_dhcp=ip, queue=queue) 
    
    
    """current_url = driver.current_url"""


