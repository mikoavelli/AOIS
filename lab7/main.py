from functools import cache


@cache
def sum_binary(num_1: str, num_2: str) -> str:
    binary_1, binary_2 = num_1[::-1] + '0', num_2[::-1] + '0'
    result: str = ''
    add_term: int = 0
    for i in range(len(binary_1)):
        current_sum: int = add_term + int(binary_1[i]) + int(binary_2[i])
        if current_sum >= 2:
            add_term = 1
            result += str(current_sum - 2)
        else:
            add_term = 0
            result += str(current_sum)
    return result[::-1]


@cache
def is_equal(word_1: str, word_2: str) -> bool:
    g: int = False
    l: int = False
    el: int = 15
    while el != -1:
        g_copy = g
        l_copy = l
        g = g_copy or (not bool(int(word_1[el])) and bool(int(word_2[el])) and not l_copy)
        l = l_copy or (bool(int(word_1[el])) and not bool(int(word_2[el])) and not g_copy)
        el -= 1
        if g != l:
            return False
    return True


class Matrix:
    def __init__(self) -> None:
        self.matrix: list[list[int]] = [[0 for _ in range(16)] for _ in range(16)]

    def print_matrix(self) -> None:
        print('\t 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15')
        for i, row in enumerate(range(16)):
            print(str(i).ljust(3), self.matrix[row])

    def add_word(self, word: str, index: int) -> None:
        _index: int = index
        for _ in range(16):
            self.matrix[_index % 16][index] = int(word[_index - index])
            _index += 1

    def add_address(self, word: str, index: int) -> None:
        _index: int = index
        for el in range(16):
            self.matrix[_index % 16][(_index - index) % 16] = int(word[el])
            _index += 1

    def get_word(self, index: int) -> dict:
        result: str = ''
        _index: int = index
        for _ in range(16):
            result += str(self.matrix[_index % 16][index])
            _index += 1
        return {'word': result, 'index': index}

    def get_address(self, index: int) -> str:
        result: str = ''
        _index: int = index
        for el in range(16):
            result += str(self.matrix[_index % 16][(_index - index) % 16])
            _index += 1
        return result

    def first_argument_ban(self, word_1_index: int, word_2_index: int, index: int) -> None:
        word_1: str = self.get_word(word_1_index)['word']
        word_2: str = self.get_word(word_2_index)['word']
        word: str = ''.join([str(int(bool(int(word_1[el]) and not bool(int(word_2[el]))))) for el in range(16)])
        self.add_word(word, index)

    def disjuction(self, word_1_index: int, word_2_index: int, index: int) -> None:
        word_1: str = self.get_word(word_1_index)['word']
        word_2: str = self.get_word(word_2_index)['word']
        word: str = ''.join([str(int(bool(int(word_1[el]) or bool(int(word_2[el]))))) for el in range(16)])
        self.add_word(word, index)

    def pierce_operation(self, word_1_index: int, word_2_index: int, index: int) -> None:
        word_1: str = self.get_word(word_1_index)['word']
        word_2: str = self.get_word(word_2_index)['word']
        word: str = ''.join([str(int(not (bool(int(word_1[el])) or bool(int(word_2[el]))))) for el in range(16)])
        self.add_word(word, index)

    def implication_first_to_second(self, word_1_index: int, word_2_index: int, index: int) -> None:
        word_1: str = self.get_word(word_1_index)['word']
        word_2: str = self.get_word(word_2_index)['word']
        word: str = ''.join([str(int((not bool(int(word_1[el])) or bool(int(word_2[el]))))) for el in range(16)])
        self.add_word(word, index)

    def find_word_in_interval(self, index_1: int, index_2: int, word: str) -> int:
        for word_index in range(index_1, index_2 + 1):
            if is_equal(word, self.get_word(word_index)['word']):
                return word_index
        return -1

    def sum_field_in_words(self, key: str) -> bool:
        words: list[dict] = [self.get_word(el) for el in range(16) if self.get_word(el)['word'].startswith(key)]
        if not words:
            return False
        for word in words:
            a: str = word['word'][3: 7]
            b: str = word['word'][7: 11]
            s: str = sum_binary(a, b)
            self.add_word(key + a + b + s, word['index'])
        return True
