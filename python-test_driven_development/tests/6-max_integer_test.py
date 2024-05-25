import unittest

max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):

    def test_max_at_the_end(self):
        self.assertEqual((max_integer([1, 2, 3, 4])), 4)

    def test_max_at_the_beginning(self):
        self.assertEqual((max_integer([4, 2, 3, 1])), 4)

    def test_max_in_the_middle(self):
        self.assertEqual((max_integer([0, 2, 4, 1, 3])), 4)

    def test_one_negative_number(self):
        self.assertEqual((max_integer([0, 2, 4, -1, 3])), 4)

    def test_only_negative_numbers(self):
        self.assertEqual((max_integer([-2, -4, -1, -3])), -1)

    def test_list_of_one_element(self):
        self.assertEqual((max_integer([-3])), -3)

    def test_list_is_empty(self):
        self.assertEqual((max_integer([])), None)


if __name__ == '__main__':
    unittest.main()
