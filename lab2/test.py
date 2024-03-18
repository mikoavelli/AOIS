import unittest

from main import *


class MyTestCase(unittest.TestCase):
    def test_infix_to_rpn(self):
        self.assertEqual(infix_to_rpn("(a | b) & !c"), "ab|c!&")
        self.assertEqual(infix_to_rpn("!((!a) & (b & (a | c)))"), "a!bac|&&!")
        self.assertEqual(infix_to_rpn("(((a->b)&(c->d))&((!a)|(d)))->((!a)|(c))"), "ab>cd>&a!d|&a!c|>")

    def test_solve_rpn_expression(self):
        self.assertEqual(solve_rpn_expression("10|1!&"), 0)
        self.assertEqual(solve_rpn_expression("1!010|&&!"), 1)
        self.assertEqual(solve_rpn_expression("10>11>&1!0|&1!1|>"), 1)

    def test_get_variables(self):
        self.assertEqual(get_variables("!a"), ('a',))
        self.assertEqual(get_variables("!a | b"), ('a', 'b'))
        self.assertEqual(get_variables("(a | b) & !c"), ('a', 'b', 'c'))
        self.assertEqual(get_variables("((a | b) & !c) -> d"), ('a', 'b', 'c', 'd'))
        self.assertEqual(get_variables("(((a | b) & !c) -> d) | !e"), ('a', 'b', 'c', 'd', 'e'))

    def test_get_solution(self):
        self.assertEqual(get_solution("((a | b) & !c) -> d", ('a', 'b', 'c', 'd')),
                         (((0, 0, 0, 0), 1),
                          ((0, 0, 0, 1), 1),
                          ((0, 0, 1, 0), 1),
                          ((0, 0, 1, 1), 1),
                          ((0, 1, 0, 0), 0),
                          ((0, 1, 0, 1), 1),
                          ((0, 1, 1, 0), 1),
                          ((0, 1, 1, 1), 1),
                          ((1, 0, 0, 0), 0),
                          ((1, 0, 0, 1), 1),
                          ((1, 0, 1, 0), 1),
                          ((1, 0, 1, 1), 1),
                          ((1, 1, 0, 0), 0),
                          ((1, 1, 0, 1), 1),
                          ((1, 1, 1, 0), 1),
                          ((1, 1, 1, 1), 1)))
        self.assertEqual(get_solution("(((a | b) & !c) -> d) | !e", ('a', 'b', 'c', 'd', 'e')),
                         (((0, 0, 0, 0, 0), 1),
                          ((0, 0, 0, 0, 1), 1),
                          ((0, 0, 0, 1, 0), 1),
                          ((0, 0, 0, 1, 1), 1),
                          ((0, 0, 1, 0, 0), 1),
                          ((0, 0, 1, 0, 1), 1),
                          ((0, 0, 1, 1, 0), 1),
                          ((0, 0, 1, 1, 1), 1),
                          ((0, 1, 0, 0, 0), 1),
                          ((0, 1, 0, 0, 1), 0),
                          ((0, 1, 0, 1, 0), 1),
                          ((0, 1, 0, 1, 1), 1),
                          ((0, 1, 1, 0, 0), 1),
                          ((0, 1, 1, 0, 1), 1),
                          ((0, 1, 1, 1, 0), 1),
                          ((0, 1, 1, 1, 1), 1),
                          ((1, 0, 0, 0, 0), 1),
                          ((1, 0, 0, 0, 1), 0),
                          ((1, 0, 0, 1, 0), 1),
                          ((1, 0, 0, 1, 1), 1),
                          ((1, 0, 1, 0, 0), 1),
                          ((1, 0, 1, 0, 1), 1),
                          ((1, 0, 1, 1, 0), 1),
                          ((1, 0, 1, 1, 1), 1),
                          ((1, 1, 0, 0, 0), 1),
                          ((1, 1, 0, 0, 1), 0),
                          ((1, 1, 0, 1, 0), 1),
                          ((1, 1, 0, 1, 1), 1),
                          ((1, 1, 1, 0, 0), 1),
                          ((1, 1, 1, 0, 1), 1),
                          ((1, 1, 1, 1, 0), 1),
                          ((1, 1, 1, 1, 1), 1)))

    def test_get_scnf_sdnf(self):
        exp1: str = "(a | b) & !c"
        exp2: str = "(a -> b) & (!a ~ c)"
        variables: tuple = ('a', 'b', 'c')
        solution1: tuple = get_solution(exp1, variables)
        solution2: tuple = get_solution(exp2, variables)

        self.assertEqual(get_sdnf_scnf_forms(solution1, variables),
                         {
                             'sdnf': (('!a', 'b', '!c'),
                                      ('a', '!b', '!c'),
                                      ('a', 'b', '!c')),
                             'sknf': (('a', 'b', 'c'),
                                      ('a', 'b', '!c'),
                                      ('a', '!b', '!c'),
                                      ('!a', 'b', '!c'),
                                      ('!a', '!b', '!c'))
                         })
        self.assertEqual(get_sdnf_scnf_forms(solution2, variables),
                         {
                             'sdnf': (('!a', '!b', 'c'),
                                      ('!a', 'b', 'c'),
                                      ('a', 'b', '!c')),
                             'sknf': (('a', 'b', 'c'),
                                      ('a', '!b', 'c'),
                                      ('!a', 'b', 'c'),
                                      ('!a', 'b', '!c'),
                                      ('!a', '!b', '!c'))
                         })

    def test_get_index_numeric_forms(self):
        exp1: str = "(a | b) & !c"
        exp2: str = "((a | b) & !c) -> d"
        exp3: str = "(((a | b) & !c) -> d) | !e"
        variables1: tuple = ('a', 'b', 'c')
        variables2: tuple = ('a', 'b', 'c', 'd')
        variables3: tuple = ('a', 'b', 'c', 'd', 'e')
        solution1: tuple = get_solution(exp1, variables1)
        solution2: tuple = get_solution(exp2, variables2)
        solution3: tuple = get_solution(exp3, variables3)

        self.assertEqual(get_index_numeric_forms(solution1),
                         {
                             'index': '00101010',
                             'numeric': ((0, 1, 3, 5, 7),
                                         (2, 4, 6))})
        self.assertEqual(get_index_numeric_forms(solution2),
                         {
                             'index': '1111011101110111',
                             'numeric': ((4, 8, 12),
                                         (0, 1, 2, 3, 5, 6, 7, 9, 10, 11,
                                          13, 14, 15))})
        self.assertEqual(get_index_numeric_forms(solution3),
                         {
                             'index': '11111111101111111011111110111111',
                             'numeric': ((9, 17, 25),
                                         (0, 1, 2, 3, 4, 5, 6, 7, 8, 10,
                                          11, 12, 13, 14, 15, 16, 18, 19, 20, 21,
                                          22, 23, 24, 26, 27, 28, 29, 30, 31))})

    def test_do_all_operations(self):
        self.assertEqual(do_all_operations("(a | b) & !c",
                                           get_sdnf_scnf=True,
                                           get_index_numeric=True),
                         {
                             'index': '00101010',
                             'numeric': ((0, 1, 3, 5, 7), (2, 4, 6)),
                             'sdnf': (('!a', 'b', '!c'), ('a', '!b', '!c'), ('a', 'b', '!c')),
                             'sknf': (('a', 'b', 'c'),
                                      ('a', 'b', '!c'),
                                      ('a', '!b', '!c'),
                                      ('!a', 'b', '!c'),
                                      ('!a', '!b', '!c'))})
        self.assertEqual(do_all_operations("!((!a) & (b & (a | c)))",
                                           get_sdnf_scnf=True,
                                           get_index_numeric=True),
                         {
                             'index': '11101111',
                             'numeric': ((3,), (0, 1, 2, 4, 5, 6, 7)),
                             'sdnf': (('!a', '!b', '!c'),
                                      ('!a', '!b', 'c'),
                                      ('!a', 'b', '!c'),
                                      ('a', '!b', '!c'),
                                      ('a', '!b', 'c'),
                                      ('a', 'b', '!c'),
                                      ('a', 'b', 'c')),
                             'sknf': (('a', '!b', '!c'),)})
        self.assertEqual(do_all_operations("(((a -> b) & (c -> d)) & !e) ~ a",
                                           get_sdnf_scnf=True,
                                           get_index_numeric=True),
                         {
                             'index': '01011101010111010000000010100010',
                             'numeric': ((0, 2, 6, 8, 10, 14, 16, 17, 18, 19,
                                          20, 21, 22, 23, 25, 27, 28, 29, 31),
                                         (1, 3, 4, 5, 7, 9, 11, 12, 13, 15, 24, 26, 30)),
                             'sdnf': (('!a', '!b', '!c', '!d', 'e'),
                                      ('!a', '!b', '!c', 'd', 'e'),
                                      ('!a', '!b', 'c', '!d', '!e'),
                                      ('!a', '!b', 'c', '!d', 'e'),
                                      ('!a', '!b', 'c', 'd', 'e'),
                                      ('!a', 'b', '!c', '!d', 'e'),
                                      ('!a', 'b', '!c', 'd', 'e'),
                                      ('!a', 'b', 'c', '!d', '!e'),
                                      ('!a', 'b', 'c', '!d', 'e'),
                                      ('!a', 'b', 'c', 'd', 'e'),
                                      ('a', 'b', '!c', '!d', '!e'),
                                      ('a', 'b', '!c', 'd', '!e'),
                                      ('a', 'b', 'c', 'd', '!e')),
                             'sknf': (('a', 'b', 'c', 'd', 'e'),
                                      ('a', 'b', 'c', '!d', 'e'),
                                      ('a', 'b', '!c', '!d', 'e'),
                                      ('a', '!b', 'c', 'd', 'e'),
                                      ('a', '!b', 'c', '!d', 'e'),
                                      ('a', '!b', '!c', '!d', 'e'),
                                      ('!a', 'b', 'c', 'd', 'e'),
                                      ('!a', 'b', 'c', 'd', '!e'),
                                      ('!a', 'b', 'c', '!d', 'e'),
                                      ('!a', 'b', 'c', '!d', '!e'),
                                      ('!a', 'b', '!c', 'd', 'e'),
                                      ('!a', 'b', '!c', 'd', '!e'),
                                      ('!a', 'b', '!c', '!d', 'e'),
                                      ('!a', 'b', '!c', '!d', '!e'),
                                      ('!a', '!b', 'c', 'd', '!e'),
                                      ('!a', '!b', 'c', '!d', '!e'),
                                      ('!a', '!b', '!c', 'd', 'e'),
                                      ('!a', '!b', '!c', 'd', '!e'),
                                      ('!a', '!b', '!c', '!d', '!e'))}
                         )
