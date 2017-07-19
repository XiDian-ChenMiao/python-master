# coding:utf-8


class Stack:
    """
    模拟栈类
    """
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def push(self, content):
        if self.full():
            print('Stack is full.')
        else:
            self.stack.append(content)
            self.top += 1

    def pop(self):
        if self.empty():
            print('Stack is empty')
        else:
            data = self.stack[self.top]
            self.top -= 1
            return data

    def full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def empty(self):
        if self.top == -1:
            return True
        else:
            return False


if __name__ == '__main__':
    stack = Stack(5)
    stack.push('Chen Miao')
    stack.push(1)
    stack.push(1.2)

    print('栈顶位置为：', stack.pop())
