from concurrent.futures import thread
from threading import current_thread


# without extending thread class 

from threading import *

class myThred:
    def myFunc(self):
        for _ in range(6):
            print("Child executing..", current_thread().getName())

obj = myThred()

t1 = Thread(target=obj.myFunc)

t1.start()
t1.join()

print("Bye", current_thread().getName())