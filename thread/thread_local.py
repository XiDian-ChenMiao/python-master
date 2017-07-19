from threading import Thread, current_thread, local

global_data = local()


def echo():
    num = global_data.num
    print('thread ', current_thread().name, ' result ', num)


def calc():
    print('thread %s is running' % current_thread().name)
    global_data.num = 0
    for _ in range(10000):
        global_data.num += 1
    echo()
    print('thread %s ended' % current_thread().name)


if __name__ == '__main__':
    print('thread %s is running' % current_thread().name)
    threads = []
    for i in range(5):
        threads.append(Thread(target=calc))
        threads[i].start()

    for i in range(5):
        threads[i].join()

    print('thread %s ended' % current_thread().name)
