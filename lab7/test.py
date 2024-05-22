import unittest
from main import Matrix


class MyTestCase(unittest.TestCase):
    @staticmethod
    def _get_matrix() -> Matrix:
        m: Matrix = Matrix()
        m.add_word('1011100010111111', 1)
        m.add_word('1011010111101001', 2)
        m.add_word('1010111001000011', 3)
        m.add_word('1010110101010101', 4)
        m.add_word('1010111100000101', 5)
        m.add_address('1011100010111111', 1)
        m.add_address('1011010111101001', 3)
        m.add_address('1010111001000011', 5)
        m.add_address('1010110101010101', 7)
        m.add_address('1010111100000101', 9)
        m.print_matrix()
        return m

    def test_get_word(self):
        m: Matrix = self._get_matrix()
        self.assertEqual(m.get_word(4)['word'], '1110110101010101')
        self.assertEqual(m.get_word(6)['word'], '0000010001000000')

    def test_get_column(self):
        m: Matrix = self._get_matrix()
        self.assertEqual(m.get_address(4), '0101110000000000')
        self.assertEqual(m.get_address(6), '0001010000000000')

    def test_first_argument_ban(self):
        m: Matrix = self._get_matrix()
        m.first_argument_ban(1, 3, 5)
        m.first_argument_ban(2, 4, 6)
        self.assertEqual(m.get_word(5)['word'], '0000000010111100')
        self.assertEqual(m.get_word(6)['word'], '0001000010101000')

    def test_disjuction(self):
        m: Matrix = self._get_matrix()
        m.disjuction(1, 3, 5)
        m.disjuction(2, 4, 6)
        self.assertEqual(m.get_word(5)['word'], '1111101010111111')
        self.assertEqual(m.get_word(6)['word'], '1111110111111101')

    def test_pierce_operation(self):
        m: Matrix = self._get_matrix()
        m.pierce_operation(1, 3, 5)
        m.pierce_operation(2, 4, 6)
        self.assertEqual(m.get_word(5)['word'], '0000010101000000')
        self.assertEqual(m.get_word(6)['word'], '0000001000000010')

    def test_implication_first_to_second(self):
        m: Matrix = self._get_matrix()
        m.implication_first_to_second(1, 3, 5)
        m.implication_first_to_second(2, 4, 6)
        self.assertEqual(m.get_word(5)['word'], '1111111101000011')
        self.assertEqual(m.get_word(6)['word'], '1110111101010111')

    def test_find_word_in_interval(self):
        m: Matrix = self._get_matrix()
        self.assertEqual(m.find_word_in_interval(1, 3, '1111101000000011'), 3)
        self.assertEqual(m.find_word_in_interval(1, 2, '1111101000000011'), -1)
        self.assertEqual(m.find_word_in_interval(1, 10, '0001010100000000'), 9)

    def test_sum_field_in_words(self):
        m: Matrix = self._get_matrix()
        self.assertEqual(m.get_word(1)['word'], '1010100010111111')
        self.assertEqual(m.get_word(5)['word'], '1011111101000101')
        self.assertTrue(m.sum_field_in_words('101'))
        self.assertEqual(m.get_word(1)['word'], '1010100010101001')
        self.assertEqual(m.get_word(5)['word'], '1011111101011001')
        self.assertFalse(m.sum_field_in_words('011'))
