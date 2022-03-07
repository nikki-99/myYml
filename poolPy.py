from multiprocessing import Pool
import time

count = 50000000

def countFunc(n):
    while n:
        n-=1



if __name__=='__main__':
    pool = Pool(processes=2)
    start = time.time()

    r1 = pool.apply_async(countFunc,[count//2])
    r2 = pool.apply_async(countFunc,[count//2])
    # countFunc(count)

    # t1 = threading.Thread(target=countFunc, args=[count//2])
    # t2 = threading.Thread(target=countFunc,args=[count//2])

    # t1.start()
    # t2.start()
    pool.close()
    pool.join()

    # t1.join()
    # t2.join()

    end = time.time()

    print(f'Total Time {end-start} sec')