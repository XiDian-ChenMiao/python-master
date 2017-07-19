# coding:utf-8
class Pointer:
    """
    二维点类
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pointer(self.x + other.x, self.y + other.y)

    def info(self):
        print('X=', self.x, 'Y=', self.y)


class D3Pointer(Pointer):
    """
    三维坐标点类
    """

    def __init__(self, x, y, z):
        super(D3Pointer, self).__init__(x, y)
        self.z = z

    def __add__(self, other):
        return D3Pointer(self.x + other.x, self.y + other.y, self.z + other.z)

    def info(self):
        print('X=', self.x, 'Y=', self.y, 'Z=', self.z)


def add_point(a, b):
    return a + b


if __name__ == '__main__':
    one = Pointer(2, 3)
    two = Pointer(4, 5)

    add_point(one, two).info()

    one3 = D3Pointer(1, 2, 3)
    two3 = D3Pointer(4, 5, 6)
    add_point(one3, two3).info()
