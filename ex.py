import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting "+ self.name+"\n")
        print_time(self.name, self.counter, 5)
        print("Exiting "+ self.name+"\n")

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s %s" %(threadName, time.ctime(time.time()), counter)+ "\n")
        counter-=1

t1 = myThread(1,"Thread1",1)
t2 = myThread(2,"Thread2",1.5)

t1.start()
t2.start()

t1.join()
t2.join()

print("Exiting Main Thread")
