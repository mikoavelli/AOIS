import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_to_binary(self):
        self.assertEqual(to_binary_direct(12), '0000000000001100')
        self.assertEqual(to_binary_direct(-12), '1000000000001100')
        self.assertEqual(to_binary_reverse(12), '0000000000001100')
        self.assertEqual(to_binary_reverse(-12), '1111111111110011')
        self.assertEqual(to_binary_additional(12), '0000000000001100')
        self.assertEqual(to_binary_additional(-12), '1111111111110100')

    def test_from_binary(self):
        self.assertEqual(from_binary('11110100', 'a'), -12)
        self.assertEqual(from_binary('1111111111110100', 'a'), -12)
        self.assertEqual(from_binary('1111111111110011', 'r'), -12)
        self.assertEqual(from_binary('00001100', 'd'), 12)

    def test_sum_binary(self):
        self.assertEqual(sum_binary(12, 25), '0000000000100101')
        self.assertEqual(sum_binary(12, -25), '1111111111110011')
        self.assertEqual(sum_binary(12, -7), '0000000000000101')
        self.assertEqual(sum_binary(-12, 25), '0000000000001101')
        self.assertEqual(sum_binary(-31, 25), '1111111111111010')
        self.assertEqual(sum_binary(-31, -25), '1111111111001000')

    def test_difference_binary(self):
        self.assertEqual(difference_binary(12, 25), '1111111111110011')
        self.assertEqual(difference_binary(12, 5), '0000000000000111')
        self.assertEqual(difference_binary(12, -7), '0000000000010011')
        self.assertEqual(difference_binary(-12, 25), '1111111111011011')
        self.assertEqual(difference_binary(-31, -25), '1111111111111010')
        self.assertEqual(difference_binary(-18, -25), '0000000000000111')

    def test_multiplication_binary(self):
        self.assertEqual(multiplication_binary(12, 25), '0000000100101100')
        self.assertEqual(multiplication_binary(12, -5), '1000000000111100')
        self.assertEqual(multiplication_binary(-12, 7), '1000000001010100')
        self.assertEqual(multiplication_binary(-12, -25), '0000000100101100')
        self.assertEqual(multiplication_binary(18, 0), '0000000000000000')
        self.assertEqual(multiplication_binary(-31, 0), '0000000000000000')

    def test_division_binary(self):
        self.assertEqual(division_binary(24, 8), '01000000010000000000000000000000')
        self.assertEqual(division_binary(15, 4), '01000000011100000000000000000000')
        self.assertEqual(division_binary(-4, 5), '00111111010011001100110011001100')
        self.assertEqual(division_binary(0, 13), '00000000000000000000000000000000')
        with self.assertRaises(ValueError):
            division_binary(13, 0)
        self.assertEqual(division_binary(-15, -6), '01000000001000000000000000000000')

    def test_to_binary_float(self):
        self.assertEqual(to_binary_float(0.125), '00111110000000000000000000000000')
        self.assertEqual(to_binary_float(1.0625), '00111111100010000000000000000000')
        self.assertEqual(to_binary_float(12.8), '01000001010011001100110011001100')
        self.assertEqual(to_binary_float(-0.75), '10111111010000000000000000000000')
        self.assertEqual(to_binary_float(-1.875), '10111111111100000000000000000000')
        self.assertEqual(to_binary_float(-15.935), '11000001011111101111010111000010')
        self.assertEqual(to_binary_float(0), '00000000000000000000000000000000')

    def test_from_binary_float(self):
        self.assertEqual(from_binary_float('00111110000000000000000000000000'), 0.125)
        self.assertEqual(from_binary_float('00111111100010000000000000000000'), 1.0625)
        self.assertEqual(from_binary_float('01000001010011001100110011001100'), 12.799999237060547)
        self.assertEqual(from_binary_float('10111111010000000000000000000000'), -0.75)
        self.assertEqual(from_binary_float('10111111111100000000000000000000'), -1.875)
        self.assertEqual(from_binary_float('11000001011111101111010111000010'), -15.934999465942383)

    def test_sum_binary_float(self):
        self.assertEqual(sum_binary_float(12.5, 2.125), '01000001011010100000000000000000')
        self.assertEqual(sum_binary_float(3.25, 0), '01000000010100000000000000000000')
        self.assertEqual(sum_binary_float(0.625, 12.25), '01000001010011100000000000000000')
        self.assertEqual(sum_binary_float(0.125, 0.5), '00111111001000000000000000000000')
        self.assertEqual(sum_binary_float(0.375, 0), '00111110110000000000000000000000')
