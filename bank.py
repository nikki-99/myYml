import threading
import time

class BankAccount():
    def __init__(self, name, balance):
        self.name=name
        self.balance = balance

    def __str__(self):
        return self.name

a1 = BankAccount("Account1",100)
a2 = BankAccount("Account2", 0)

lock = threading.Lock()

class BankTransferThread(threading.Thread):
    def __init__(self, sender, receiver, amount):
        threading.Thread.__init__(self)
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def run(self):
        lock.acquire()
        sender_balance = self.sender.balance - self.amount
        time.sleep(0.001)
        self.sender.balance = sender_balance

        receiver_balance = self.receiver.balance + self.amount
        time.sleep(0.001)
        self.receiver.balance = receiver_balance
        lock.release()

if __name__ =='__main__':
    threads=[]
    
    for i in range(100):
        t = BankTransferThread(a1,a2,1)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(a1.balance)
    print(a2.balance)