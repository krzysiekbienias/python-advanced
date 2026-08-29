import multiprocessing
from multiprocessing import Process

def do_work():
    print("starting word")
    i=0
    for _ in range(80000000):
        i+=1
    print("finished work")

if __name__=="__main__":
    multiprocessing.set_start_method("fork")
    for _ in range(5):
        p=Process(target=do_work,args=())
        p.start()