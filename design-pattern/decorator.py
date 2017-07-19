# coding:utf-8
class Door:
    """
    待装饰的门类
    """
    def __init__(self):
        pass

    def open(self):
        print('Open Door')

    def close(self):
        print('Close Door')


class DoorDecorater:
    """
    装饰器模式测试
    """
    def __init__(self, door):
        self.door = door

    def open(self):
        print('DAQINZHIDI ')
        self.door.open()

    def close(self):
        print('Chen Miao')
        self.door.close()


if __name__ == '__main__':
    door = Door()
    door_deco = DoorDecorater(door)
    door_deco.open()
    door_deco.close()
