import unittest2
from day_03 import *

class TestFactorialMethods(unittest2.TestCase):

    def test_division(self):
        self.assertEqual(division(4, 3), 1)
   
    def test_division_float(self):
        self.assertEqual(division_float(4, 3), 1.3333333333333333)

if __name__ == '__main__':
    unittest2.main()

