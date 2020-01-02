import unittest2
from day_01 import *

class TestFactorialMethods(unittest2.TestCase):

    def test_conditional_test_odd_even(self):
        self.assertTrue(conditional_test_odd_even(4), None)
        self.assertFalse(conditional_test_odd_even(1), None)

    def test_conditional_test_range_2_5(self):
        self.assertEqual(conditional_test_range_2_5(2), "Not Weird")
        self.assertEqual(conditional_test_range_2_5(3), "Not Weird")
        self.assertEqual(conditional_test_range_2_5(8), "Weird")
        self.assertEqual(conditional_test_range_2_5(20), "Weird")
        self.assertEqual(conditional_test_range_2_5(21), "Not Weird")

if __name__ == '__main__':
    unittest2.main()