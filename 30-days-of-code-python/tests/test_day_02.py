import unittest2
from day_02 import *

class TestFactorialMethods(unittest2.TestCase):

    def test_sum(self):
        self.assertEqual(sum(3, 2), 5)

    def test_difference(self):
        self.assertEqual(difference(3, 2), 1)
    
    def test_product(self):
        self.assertEqual(product(3, 2), 6)

if __name__ == '__main__':
    unittest2.main()
