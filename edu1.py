# By extending thread class 

import threading

class myThread(threading.Thread):
    def run(self):
        for _ in range(6):
            print("Child executing..", threading.current_thread().getName())

t1 = myThread()
t1.start()

t1.join()

print("Bye", threading.current_thread().getName())