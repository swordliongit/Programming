from queue import Queue
from _module import func
import threading
from datetime import datetime

from selenium import webdriver



"""# List of URLs to scrape
urls = ['http://192.168.5.1/cgi-bin/luci', 'http://192.168.5.2/cgi-bin/luci']

def scrape_website(url):
  # Create a new browser instance
  browser = webdriver.Chrome()
  # Navigate to the URL
  browser.get(url)
  # Perform the scraping here
  # ...
  # Close the browser when finished
  browser.quit()

# Create a new thread for each URL
for url in urls:
  t = threading.Thread(target=scrape_website, args=(url,))
  t.start()
"""




    

#env['modem.profile'].search([x_update_date,"<",datetime.datetime.now()]).unlink()

queue = Queue()


threads = []

for i in range(0, 5):
    t = threading.Thread(target=func, args=(i, queue))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
    
for t in threads:
    print(queue.get())



