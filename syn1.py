from concurrent.futures import thread
import threading
import time

class myThread(threading.Thread):
    def __init__(self, thraedID, name, count):
        threading.Thread.__init__(self)
        self.threadID = thraedID
        self.name = name
        self.count = count

    def run(self):
        print("Starting "+self.name+"\n")
        threadLock.acquire()
        print_time(self.name,1,self.count)
        threadLock.release()
        print("Exiting "+self.name+"\n")


class myThread2(threading.Thread):
    def __init__(self, thraedID, name, count):
        threading.Thread.__init__(self)
        self.threadID = thraedID
        self.name = name
        self.count = count

    def run(self):
        print("Starting "+self.name+"\n")
        threadLock.acquire()
        threadLock.release()
        print_time(self.name,1,self.count)
        print("Exiting "+self.name+"\n")



def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print("%s : %s %s" %(name, time.ctime(time.time()), count)+"\n")
        count-=1

threadLock = threading.Lock()


t2= myThread(2,"Payment",5)
t3 = myThread2(3,"Sending Email",10)
t4 = myThread2(4,"Loading page",3)


t2.start()
t3.start()
t4.start()

t2.join()
t3.join()
t4.join()

print("Exiting Main Thread"+"\n")

