import json
from threading import Thread,Lock
import urllib.request
import time

finished_count=0

def count_letters(url,frequency,mutex):
    response=urllib.request.urlopen(url)
    txt=str(response.read())
    mutex.acquire()
    for l in txt:
        letter=l.lower()
        if letter in frequency:
            val=frequency[letter]
            time.sleep(0)   # call miedzy READ a WRITE -> tu moze wskoczyc inny watek
            frequency[letter]=val+1
    global finished_count
    finished_count+=1
    mutex.release()        #increase when thread finishes

def main():
    frequency={}
    mutex=Lock()
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c]=0
    start=time.time()    
    for i in range(1000,1020):
        Thread(target=count_letters,args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt",frequency,mutex)).start() 
    
    while True:
        mutex.acquire()
        time.sleep(0.5)   
        
    print(json.dumps(frequency,indent=4))
    end=time.time()
    print("Done, time taken", end -start)
    print()

if __name__=="__main__":
    main()

