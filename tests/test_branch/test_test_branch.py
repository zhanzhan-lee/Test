import sys
import unittest


sys.path.insert(0, './code/Code')

from test_module import add_numbers

class TestTestBranch(unittest.TestCase):
    def test_add_numbers_positive(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_numbers_negative(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)

    def test_add_numbers_zero(self):
        result = add_numbers(0, 5)
        self.assertEqual(result, 5)
        result = add_numbers(0, 0)
        self.assertEqual(result, 0)

    def test_add_numbers_mixed(self):
        result = add_numbers(5, -3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
