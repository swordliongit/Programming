# pip install graphics.py -> used in the course

from threading import Thread, Lock
import urllib.request
import json
from time import sleep


def child():
    print("Child thread is doing work...")
    sleep(5)
    print("Child thread done...")


def parent():
    t = Thread(target=child)
    t.start()
    print("Parent thread is waiting...")
    t.join()
    print("Parent thread is unblocked...")
    
    
    
parent()