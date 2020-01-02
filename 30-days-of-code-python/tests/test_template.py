import unittest2
from template import *

class TestFactorialMethods(unittest2.TestCase):

    def test_template(self):
        args = ["xxx"]
        self.assertTrue(main(args))

if __name__ == '__main__':
    unittest2.main()

