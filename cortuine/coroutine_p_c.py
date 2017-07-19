import time


def consumer():
    message = ''
    while True:
        n = yield message
        if not n:
            return
        print('[CONSUMER] consuming %s' % n)
        time.sleep(2)
        message = '200 OK'


def producer(c):
    c.__next__()
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] producing ', n)
        r = c.send(n)
        print('[PRODUCER] consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    producer(c)
