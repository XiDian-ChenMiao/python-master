# coding:utf-8
import threading
import time

SHARE = 0
condition = threading.Condition()


class Producer(threading.Thread):
    def __init__(self):
        super(Producer, self).__init__()
        self.name = 'Producer'

    def run(self):
        global SHARE
        if condition.acquire():
            while True:
                if not SHARE:
                    SHARE += 1
                    print(self.name, SHARE)
                    condition.notify()
                condition.wait()
                time.sleep(1)


class Customer(threading.Thread):
    def __init__(self):
        super(Customer, self).__init__()
        self.name = 'Customer'

    def run(self):
        global SHARE
        if condition.acquire():
            while True:
                if SHARE:
                    SHARE -= 1
                    print(self.name, SHARE)
                    condition.notify()
                condition.wait()
                time.sleep(1)


if __name__ == '__main__':
    producer = Producer()
    customer = Customer()

    producer.start()
    customer.start()
