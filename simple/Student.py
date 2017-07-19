# coding:utf-8
class Student(object):
    """
    学生类的描述信息，其中包括年龄和姓名属性
    """
    '''
    类属性区
    '''
    class_attribute = 'PERSON'  # 类属性

    SPECIAL = 'ANIMAL'  # 常量信息
    __slots__ = ('name', 'age')  # 添加__slot__可以指定哪些属性从外部可以在对象上添加
    '''
    所有函数区
    '''

    @staticmethod  # 静态方法，不能引用实例对象的属性
    def country():
        print('Country:', "People's Republic of China")

    @classmethod  # 可以使用类或者类实例来引用
    def show(cls, classname):
        print('Class Name:', classname)

    @classmethod
    def get_instance(cls):
        return cls('Chen Miao')

    @property  # 属性包装器
    def name(self):
        print('Attribute Name Decorator')
        return self._name

    @name.setter
    def name(self, name):
        if 5 <= len(name) <= 16:
            self._name = name
        else:
            print('Name is not correct.')

    def __init__(self, name, age=23, gender='Male'):  # 构造函数，并且设置默认值
        self._name = name
        self.age = age
        self.__gender = gender  # 私有属性

    def set_name(self, name):
        self.name = name

    def info(self):
        print('Name', self.name, 'Age', self.age, 'Gender', self.__gender)


if __name__ == '__main__':
    student = Student('DAQINZHIDI', 23)
    student.info()
    print('Class Attribute:', student.class_attribute)
    print('Constant:', student.SPECIAL)
    student.name = 'Chen'
    student.info()
    Student.country()
    Student.get_instance().info()
    Student.show(Student.__name__)
    if not hasattr(student, 'school'):  # 利用反射进行属性操作
        setattr(student, 'school', 'XiDian')
    print('School', getattr(student, 'school'))
