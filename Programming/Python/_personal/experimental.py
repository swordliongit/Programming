from queue import Queue
from _module import func
import threading
import datetime

time = str(datetime.datetime.now())

print((time))



"""
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
"""


