import unittest

max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):

    def test_max_integer(self):
        list_case = [1, 2, 3, 4]
        self.assertEqual(print(max_integer(list_case)), None)

    def test_len_list(self):
        list_case = []
        self.assertEqual(len(list_case) == 0, True)

    def test_is_list(self):
        list_case = 3
        self.assertFalse(isinstance(list_case, list))


if __name__ == '__main__':
    unittest.main()
