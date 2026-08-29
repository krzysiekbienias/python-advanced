from threading import Thread
import time


def do_work():
    print("starting word")
    i=0
    for _ in range(80000000):
        i+=1
    print("finished work")

for _ in range(5):
    t = Thread(target=do_work,args=())
    t.start()