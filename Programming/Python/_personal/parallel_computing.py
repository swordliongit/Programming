# pip install graphics.py -> used in the course

from threading import Thread, Lock
import urllib.request
import json
import time


class StingySpendy:
    money = 100
    mutex = Lock()
    
    def Stingy(self):
        for _ in range(10000000):
            self.mutex.acquire()
            self.money += 10
            self.mutex.release()
        print("Stingy done")
        
    def Spendy(self):
        for _ in range(10000000):
            self.mutex.acquire()
            self.money -= 10
            self.mutex.release()
        print("Spendy done")     
        
ss = StingySpendy()
Thread(target=ss.Stingy, args=()).start()
Thread(target=ss.Spendy, args=()).start()
time.sleep(10)
print(ss.money)