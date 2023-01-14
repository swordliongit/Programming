# pip install graphics.py -> used in the course

import multiprocessing

from multiprocessing import Process


def do_work():
    print("Starting work")
    i = 0
    for _ in range(20000000):
        i += 1
    print("Finished work")
    
    
if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    for _ in range(0, 5):
        p = Process(target=do_work)
        p.start()

# import time
# from threading import Thread


# def do_work():
#     print("Starting work")
#     time.sleep(1)
#     print("Finished work")


# for _ in range(5):
#     t = Thread(target=do_work, args=())
#     t.start()



