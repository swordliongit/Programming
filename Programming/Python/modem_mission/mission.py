from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

from time import sleep

def login():

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "login_in").click() # login button
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/form/div[3]/button[1]"))).click()


    #WebDriverWait(driver, 5).until(lambda driver: "http://192.168.1.1/cgi-bin/luci/admin/" != driver.current_url)
    
    
        
# info
username = "R3000admin"
password = "admin"

# site to log in
url = "http://192.168.5.1/cgi-bin/luci"


from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless") # silent browser

# our driver
from selenium import webdriver
driver = webdriver.Chrome("chromedriver", options=chrome_options)

# open the url
driver.get(url)

# find the elements we want to fill in

login() #login the site


############################# XXX
print("Logged in successfully")
sleep(1)
############################# XXX

# go to another page
driver.find_element(By.LINK_TEXT, "Network").click()
sleep(1)

# go to another page
driver.find_element(By.LINK_TEXT, "Time Synchronisation").click()
sleep(1)

# find the text field
txt_field = driver.find_element(By.ID, "cbid.ntpclient.cfg04887d.manual_time")
txt_field.click()
txt_field.send_keys(Keys.CONTROL + "a") # select all
txt_field.send_keys(Keys.DELETE) 
txt_field.send_keys("2016-04-23 12:00:39") # change

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "cbi.apply"))).click() # Apply button

############################# XXX
print("Changed successfully")
############################# XXX