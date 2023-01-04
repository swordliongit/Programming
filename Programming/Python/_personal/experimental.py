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


import threading
import queue

q = queue.Queue()

item_list = [1, 2, 3, 4, 5]

threads = []

for item in item_list:
    t = threading.Thread(target=func, args=(item, q))
    threads.append(t)
    t.start()


for t in threads:
    t.join()


for i in range(0, len(item_list)):
    print(q.get())
