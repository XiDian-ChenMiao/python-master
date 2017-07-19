# coding:utf-8


class Queue:
    """
    模拟队列类
    """
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.head = -1
        self.tail = -1

    def empty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def full(self):
        if self.tail - self.head == self.size:
            return True
        else:
            return False

    def enqueue(self, content):
        if self.full():
            print('Queue is full.')
        else:
            self.queue.append(content)
            self.tail += 1

    def dequeue(self):
        if self.empty():
            print('Queue is empty')
        else:
            self.head += 1
            data = self.queue[self.head]
            return data


if __name__ == '__main__':
    queue = Queue(10)
    queue.enqueue(1.2)
    queue.enqueue('DAQINZHIDI')
    queue.enqueue({'Name': '陈苗'})

    print('Dequeue:', queue.dequeue())
