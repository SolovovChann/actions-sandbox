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


class AddMul(unittest.TestCase):
    def test_mul_1_and_1(self):
        self.assertEqual(calculator.mul(1, 1), 1)

    def test_mul_10_and_0(self):
        self.assertEqual(calculator.mul(10, 0), 0)

    def test_mul_1000_and_5000(self):
        self.assertEqual(calculator.mul(1000, 5000), 5000000)


class AddDiv(unittest.TestCase):
    def test_div_1_to_1(self):
        self.assertEqual(calculator.div(1, 1), 1)

    def test_div_10_to_2(self):
        self.assertEqual(calculator.div(10, 5), 2)

    def test_div_1_to_100(self):
        self.assertAlmostEqual(calculator.div(1, 100), 0.01, 1)

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, calculator.div, 10, 0)
