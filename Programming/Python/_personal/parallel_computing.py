# pip install graphics.py -> used in the course
from threading import Thread, Lock
import os
from os.path import isdir, join
from time import perf_counter

matches = []
mutex = Lock()

def file_search(root, filename):
    
    child_threads = []
    
    print("Searching in:", root)
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            t = Thread(target=file_search, args=(full_path, filename))
            t.start()
            child_threads.append(t)
    for t in child_threads:
        t.join()
    # print (os.listdir(root))
    
def main():
    # print(os.listdir("C:/odoo-15/odoo/"))
    start = perf_counter()
    # file_search("C:/odoo-15/odoo/", "__init__.py")
    t = Thread(target=file_search, args=("C:/odoo-15/odoo/", "__init__.py"))
    t.start()
    t.join()
    for m in matches:
        print("Matched:", m)
    end = perf_counter()
    
    print(end-start)
        
main()