from queue import Queue
from _module import func
import threading
from datetime import datetime

from selenium import webdriver




_list = [1, 2]


_list.append({'key':3})

print(_list)












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

"""d = {'a': 1, 'b': 2, 'c': 3}
lst = ['x', 'y', 'z']

for key, value, item in zip(d, d.values(), lst):
    print(key, value, item)"""