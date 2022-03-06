# time comparison 

from threading import Thread
import time

def fun1(n):
    for i in n:
        time.sleep(1)
        print(i*i)


def fun2(n):
    for i in n:
        time.sleep(1)
        print(i*i*i)

s = time.time()
n = [2,5,6,7,8]

t1 = Thread(target=fun1, args=(n,))
t2 = Thread(target=fun2, args=(n,))

t1.start()
t2.start()

t1.join()
t2.join()

e = time.time()

print("Total time ", e-s)