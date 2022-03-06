import threading
import time
from time import sleep


def cal_square(numbers):
    for n in numbers:
        print("Square ",n*n)
        sleep(1)



def cal_cube(numbers):
    for n in numbers:
        print("Cube ",n*n*n)
        sleep(1)

l=[2,3,4,5]

t=time.time()

t1 = threading.Thread(target=cal_square, args=(l,))
t2 = threading.Thread(target=cal_cube, args=(l,))


t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Time taken ", time.time()-t)
print("\n")

