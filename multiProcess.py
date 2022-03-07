import multiprocessing


# multithreading: running code concurrently
# multiprocessing: running code parallal

import time
import multiprocessing

start = time.perf_counter()

def do_something(t):
    print("Sleeping {t} sec..")
    time.sleep(t)
    print("Done sleeping.")

# p1 = multiprocessing.Process(target=do_something, args=[1])
# p2 = multiprocessing.Process(target=do_something, args=[1])

process =[]

for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1])
    p.start()
    process.append(p)

for p in process:
    p.join()

# p1.start()
# p2.start()

# p1.join()
# p2.join()

end = time.perf_counter()

print(f'Finished in {end-start} sec')



