import unittest

import calculator


class AddTest(unittest.TestCase):
    def test_add_1_and_1(self):
        self.assertEqual(calculator.add(1, 1), 2)

    def test_add_10_and_10(self):
        self.assertEqual(calculator.add(10, 10), 20)

    def test_add_1000_and_1000(self):
        self.assertEqual(calculator.add(1000, 1000), 2000)


class AddSub(unittest.TestCase):
    def test_sub_1_and_1(self):
        self.assertEqual(calculator.sub(1, 1), 0)

    def test_sub_10_and_1(self):
        self.assertEqual(calculator.sub(10, 1), 9)

    def test_sub_1000_and_5000(self):
        self.assertEqual(calculator.sub(1000, 5000), -4000)
