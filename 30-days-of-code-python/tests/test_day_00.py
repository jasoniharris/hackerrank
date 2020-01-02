import unittest2
from day_00 import *

class TestFactorialMethods(unittest2.TestCase):

    def test_output(self):
        statement="Hello, World!"
        self.assertEqual(print_out(statement), "Hello, World!")

if __name__ == '__main__':
    unittest2.main()