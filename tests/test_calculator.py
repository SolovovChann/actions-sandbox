import unittest

import calculator


class AddTest(unittest.TestCase):
    def test_add_1_and_1(self):
        self.assertEqual(calculator.add(1, 1), 2)

    def test_add_10_and_10(self):
        self.assertEqual(calculator.add(10, 10), 20)

    def test_add_1000_and_1000(self):
        self.assertEqual(calculator.add(1000, 1000), 2000)
