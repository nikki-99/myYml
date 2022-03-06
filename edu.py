# without creating a class

from threading import *

def mt():
    for _ in range(6):
        print("Child executing..", current_thread().getName())

t1=Thread(target=mt)

print(current_thread().getName())

t1.start()
t1.join()

print("Bye",current_thread().getName())