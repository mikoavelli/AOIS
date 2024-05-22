from main import Matrix


def print_operations() -> None:
    print('-' * 66)
    print('1. Add word: insert word of 16 char and index')
    print('2. Get word: insert index between 0 and 15')
    print('3. Add address: insert address of 16 char and index')
    print('4. Get address: insert index between 0 and 15')
    print('5. (f2) First argument ban: insert 3 indexes between 0 and 15')
    print('6. (f7) Disjunction: insert 3 indexes between 0 and 15')
    print('7. (f8) Pierce operation: insert 3 indexes between 0 and 15')
    print('8. (f13) Implication first to second: insert 3 indexes between 0 and 15')
    print('9. Find word in interval: insert 2 indexes between 0 and 15 and word (return first index found)')
    print('10. Sum fields in words: insert key V = 000-111')
    print('0. Exit')


def main() -> None:
    while True:
        matrix.print_matrix()
        print_operations()
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                word, index = (input('Enter your word: '),
                               int(input('Enter index: ')))
                if len(word) != 16 or word.replace('1', '0') != ''.zfill(16):
                    print('Invalid input.')
                    continue
                matrix.add_word(word, index)
            case '2':
                index = int(input('Enter index: '))
                if not 0 <= index < 16:
                    print('Invalid input.')
                    continue
                print(f'The word is: {matrix.get_word(index)['word']}')
            case '3':
                address, index = (input('Enter address: '),
                                  int(input('Enter index: ')))
                if len(address) != 16 or address.replace('1', '0') != ''.zfill(16):
                    print('Invalid input.')
                    continue
                matrix.add_address(address, index)
            case '4':
                index = int(input('Enter index: '))
                if not 0 <= index < 16:
                    print('Invalid input.')
                    continue
                print(f'The address is: {matrix.get_address(index)}')
            case '5':
                w_1, w_2, index = (int(input('Enter word 1 index: ')),
                                   int(input('Enter word 2 index: ')),
                                   int(input('Enter index: ')))
                if not 0 <= w_1 < 16 or not 0 <= w_2 < 16 or not 0 <= index < 16:
                    print('Invalid input.')
                    continue
                matrix.first_argument_ban(w_1, w_2, index)
            case '6':
                w_1, w_2, index = (int(input('Enter word 1: ')),
                                   int(input('Enter word 2: ')),
                                   int(input('Enter index: ')))
                if not 0 <= w_1 < 16 or not 0 <= w_2 < 16 or not 0 <= index < 16:
                    print('Invalid input.')
                    continue
                matrix.disjuction(w_1, w_2, index)
            case '7':
                w_1, w_2, index = (int(input('Enter word 1: ')),
                                   int(input('Enter word 2: ')),
                                   int(input('Enter index: ')))
                if not 0 <= w_1 < 16 or not 0 <= w_2 < 16 or not 0 <= index < 16:
                    print('Invalid input.')
                    continue
                matrix.pierce_operation(w_1, w_2, index)
            case '8':
                w_1, w_2, index = (int(input('Enter word 1: ')),
                                   int(input('Enter word 2: ')),
                                   int(input('Enter index: ')))
                if not 0 <= w_1 < 16 or not 0 <= w_2 < 16 or not 0 <= index < 16:
                    print('Invalid input.')
                    continue
                matrix.implication_first_to_second(w_1, w_2, index)
            case '9':
                index_1, index_2, word = (int(input('Enter index 1: ')),
                                          int(input('Enter index 2: ')),
                                          input('Enter word: '))
                if not 0 <= index_1 < 16 or not 0 <= index_2 < 16 or not len(word) == 16:
                    print('Invalid input.')
                    continue
                find_index: int = matrix.find_word_in_interval(index_1, index_2, word)
                print(f'Word found on index {find_index}' if find_index != -1 else 'Word not found')
            case '10':
                key: str = input('Enter key V = 000-111: ')
                if not len(key) == 3 or key.replace('1', '0') != ''.zfill(3):
                    print('Invalid input.')
                    continue
                matrix.sum_field_in_words(key)
            case '0':
                exit(0)
            case _:
                print('Invalid choice.')
        print('-' * 66)


if __name__ == '__main__':
    matrix: Matrix = Matrix()
    main()
