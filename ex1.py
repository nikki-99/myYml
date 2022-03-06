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
        print_time(self.name,1,self.count)
        print("Exiting :"+self.name+"\n")

def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print("%s : %s %s" %(name, time.ctime(time.time()), count)+"\n")
        count-=1

t1 = myThread(1,"Thread1",10)
t2 = myThread(2, "Thread2", 5)

t1.start()
t2.start()

t1.join()
t2.join()

print("Exiting Main Thread"+"\n")

