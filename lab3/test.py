import unittest
from calculation import calculation
from calculation_table import calculation_table
from minimization import minimization
from calculation_karno import main as karno
from sknf_sdnf import get_sknf_sdnf


class Test(unittest.TestCase):
    def test_karno(self):
        pass

    def test_calculation(self):
        expression_1: str = '(a -> b) & !c & d'
        expression_2: str = '(a -> b) & !c & (d ~ e)'

        sknf_1 = get_sknf_sdnf(expression_1)['sknf']
        sknf_2 = get_sknf_sdnf(expression_2)['sknf']
        sdnf_1 = get_sknf_sdnf(expression_1)['sdnf']
        sdnf_2 = get_sknf_sdnf(expression_2)['sdnf']

        self.assertEqual(calculation(minimization(sknf_1), False),
                         [['!a', 'b'], ['!c'], ['d']])
        self.assertEqual(calculation(minimization(sknf_2), False),
                         [['!a', 'b'], ['!c'], ['!d', 'e'], ['d', '!e']])
        self.assertEqual(calculation(minimization(sdnf_1), True),
                         [['!a', '!c', 'd'], ['b', '!c', 'd']])
        self.assertEqual(calculation(minimization(sdnf_2), True),
                         [['!a', '!c', '!d', '!e'],
                          ['!a', '!c', 'd', 'e'],
                          ['b', '!c', '!d', '!e'],
                          ['b', '!c', 'd', 'e']])

    def test_calculation_table(self):
        expression_1: str = '(a -> b) & !c & d'
        expression_2: str = '(a -> b) & !c & (d ~ e)'

        sknf_1 = get_sknf_sdnf(expression_1)['sknf']
        sknf_2 = get_sknf_sdnf(expression_2)['sknf']
        sdnf_1 = get_sknf_sdnf(expression_1)['sdnf']
        sdnf_2 = get_sknf_sdnf(expression_2)['sdnf']

        minimiz_sknf_1 = minimization(sknf_1)
        minimiz_sknf_2 = minimization(sknf_2)
        minimiz_sdnf_1 = minimization(sdnf_1)
        minimiz_sdnf_2 = minimization(sdnf_2)

        self.assertEqual(calculation_table(minimiz_sknf_1, sknf_1, False),
                         (('!a', 'b'), ('!c',), ('d',)))
        self.assertEqual(calculation_table(minimiz_sknf_2, sknf_2, False),
                         (('!a', 'b'), ('!c',), ('!d', 'e'), ('d', '!e')))
        self.assertEqual(calculation_table(minimiz_sdnf_1, sdnf_1, True),
                         (('!a', '!c', 'd'), ('b', '!c', 'd')))
        self.assertEqual(calculation_table(minimiz_sdnf_2, sdnf_2, True),
                         (('!a', '!c', '!d', '!e'),
                          ('!a', '!c', 'd', 'e'),
                          ('b', '!c', '!d', '!e'),
                          ('b', '!c', 'd', 'e')))

    def test_karno(self):
        expression_1: str = 'a -> b'
        expression_2: str = '(a -> b) & !c'
        expression_3: str = '(a -> b) & !c & d'
        expression_4: str = '(a -> b) & !c & (d ~ e)'
        self.assertEqual(karno(expression_1), {'sdnf': (('!a', 'X'), ('X', 'b')), 'sknf': (('!a', 'b'),)})
        self.assertEqual(karno(expression_2), {'sdnf': (('!a', 'X', '!c'), ('X', 'b', '!c')),
                                               'sknf': (('!a', 'b', 'X'), ('X', 'X', '!c'))})
        self.assertEqual(karno(expression_3), {'sdnf': (('!a', 'X', '!c', 'd'),
                                                        ('X', 'b', '!c', 'd')),
                                               'sknf': (
                                                   ('!a', 'b', 'X', 'X'),
                                                   ('X', 'X', '!c', 'X'),
                                                   ('X', 'X', 'X', 'd'))})
        self.assertEqual(karno(expression_4), {'sdnf': (('!a', 'X', '!c', '!d', '!e'),
                                                        ('!a', 'X', '!c', 'd', 'e'),
                                                        ('X', 'b', '!c', '!d', '!e'),
                                                        ('X', 'b', '!c', 'd', 'e')),
                                               'sknf': (('!a', 'b', 'X', 'X', 'X'),
                                                        ('X', 'X', '!c', 'X', 'X'),
                                                        ('X', 'X', 'X', '!d', 'e'),
                                                        ('X', 'X', 'X', 'd', '!e'))})
