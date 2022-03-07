import concurrent.futures
from concurrent.futures import thread
import threading
import time

start = time.perf_counter()


def do_something(sec):
    print(f"Sleeping {sec} sec..")
    time.sleep(sec)
    return f"Done sleeping {sec}."


with concurrent.futures.ThreadPoolExecutor() as executer:
    secs = [5,4,3,2,1]
    results = executer.map(do_something, secs)

    for result in results:
        print(result)

# for _ in range(6):
#     do_something()

# threads=[]
# for _ in range(6):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()







end = time.perf_counter()

print(f'Total time {end-start} sec')

