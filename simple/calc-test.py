# coding:utf-8
from calc import Calc
import unittest


class CalcTest(unittest.TestCase):

    def setUp(self):
        self.target = Calc()

    def tearDown(self):
        self.target = None

    def testAdd(self):
        self.assertEqual(self.target.add(5, 10), 15)

    def testSub(self):
        self.assertEqual(self.target.sub(5, 10), -5)

    def testMuti(self):
        self.assertEqual(self.target.muti(5, 10), 50)

    def testDiv(self):
        self.assertEqual(self.target.div(10, 5), 2)


if __name__ == '__main__':
    unittest.main()
