# time comparison 

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
fun1(n)
fun2(n)

e = time.time()

print("Total time ", e-s)