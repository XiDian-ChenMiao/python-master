# coding:utf-8
class Sequence:
    """
    模拟序列类
    """
    def __init__(self):
        self.seq = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, item):
        if 0 <= item < 16:
            return self.seq[item]


if __name__ == '__main__':
    sequence = Sequence()
    for i in range(16):
        print(sequence[i])

