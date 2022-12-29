from selenium import webdriver

def modem_login_init():
    """function to set browser to run in background, initialize driver object

    Returns:
        Chrome driver: driver to return
    """
    
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--headless") # silent browser
    
    # our driver
    
    driver = webdriver.Chrome("chromedriver", options=chrome_options)
    
    #driver = webdriver.Chrome("chromedriver")
    
    return driver

print(type(modem_login_init()))