import unittest
from tasks.elementary import *
import random


class TestMyAdd(unittest.TestCase):

    def test(self):
        number_1 = random.randint(-10, 10)
        number_2 = random.randint(-10, 10)
        self.assertEqual(my_add(number_1, number_2), number_1 + number_2)


class TestMyAbs(unittest.TestCase):

    def test(self):
        for _ in range(100):
            number = random.randint(-100, 100)
            self.assertEqual(my_abs(number), abs(number))


class TestMySum(unittest.TestCase):

    def test(self):
        arr_len = random.randint(0, 100)
        arr = [random.randint(-100, 100) for _ in range(arr_len)]
        self.assertEqual(my_sum(arr), sum(arr))


class TestMyLen(unittest.TestCase):

    def test(self):
        arr_len = random.randint(0, 100)
        arr = [0] * arr_len
        self.assertEqual(my_len(arr), len(arr))


class TestMyCount(unittest.TestCase):

    def test(self):
        arr_len = random.randint(0, 100)
        arr = [random.randint(-10, 10) for _ in range(arr_len)]
        val = random.randint(-10, 10)
        self.assertEqual(my_count(arr, val), arr.count(val))


class TestMyReverse(unittest.TestCase):

    def test(self):
        arr_len = random.randint(0, 100)
        arr = [random.randint(-10, 10) for _ in range(arr_len)]
        self.assertListEqual(my_reverse(arr), list(reversed(arr)))


class TestMySort(unittest.TestCase):

    def test(self):
        arr_len = random.randint(0, 100)
        arr = [random.randint(-10, 10) for _ in range(arr_len)]
        self.assertListEqual(my_sort(arr), sorted(arr))


class TestMyFind(unittest.TestCase):

    def test(self):
        text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed 
        do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim 
        ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
        aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
        in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum."
        """
        patterns = ['cillum dolore', 'commodo', 'synt']
        for pattern in patterns:
            self.assertEqual(my_find(text, pattern), text.find(pattern))


class TestMySptit(unittest.TestCase):

    def test(self):
        text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed 
        do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim 
        ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
        aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
        in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt 
        in culpa qui officia deserunt mollit anim id est laborum."
        """
        delimiter = random.choice(text)
        self.assertListEqual(my_split(text, delimiter), text.split(delimiter))


class TestMyRange(unittest.TestCase):

    def test_positive(self):
        range_len = random.randint(50, 100)
        range_start = random.randint(0, 9)
        range_step = random.randint(0, 10)

        self.assertListEqual(my_range(range_start, range_len, range_step),
            list(range(range_start, range_len, range_step)))
