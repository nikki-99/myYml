import threading
import time
import threading

start = time.perf_counter()

def do_something():
    print("Sleeping for 1sec \n")
    time.sleep(1)
    print("Done sleeping \n")

t1=  threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print("Finished in {} seconds".format(finish-start))