from concurrent.futures import thread
import time
import threading

read_mutex = threading.Semaphore(3)

data = "A Data Stream"

class ReaderThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        read_mutex.acquire()
        output = self.getName() + " start reading "
        print(output)
        time.sleep(0.5)
        output = self.getName() + " end reading "
        print(output)
        read_mutex.release()

if __name__ == '__main__':
    threads=[]
    for i in range(10):
        t = ReaderThread()
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        

