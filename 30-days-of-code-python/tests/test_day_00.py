import unittest2
from day_00 import *

class TestFactorialMethods(unittest2.TestCase):

    def test_output(self):
        self.assertEqual(print_out("Hello, World!"), None)

if __name__ == '__main__':
    unittest2.main()