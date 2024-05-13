import unittest

import hash_table


class TestHashTable(unittest.TestCase):
    def test_read_method(self):
        htable: hash_table.HashTable = hash_table.HashTable(10)
        self.assertEqual(htable.read('Kamar'), None)
        self.assertEqual(htable.read('Banana'), None)

    def test_create_method(self):
        htable: hash_table.HashTable = hash_table.HashTable(10)
        htable.create('banana', 'SomeText')
        htable.create('Ghisit', 'RandomText')
        htable.create('Igisit', 'NotRandomText')
        self.assertEqual(htable.read('banana'), 'SomeText')
        self.assertEqual(htable.read('Ghisit'), 'RandomText')
        self.assertEqual(htable.read('Igisit'), 'NotRandomText')

    def test_update_method(self):
        htable: hash_table.HashTable = hash_table.HashTable(10)
        htable.create('Do', 'Dot')
        htable.create('Ri', 'Risk')
        htable.create('Me', 'Metro')
        htable.update('Do', 'DownTown')
        htable.update('Ri', 'Ricardo')
        htable.update('Me', 'Milos')
        self.assertEqual(htable.read('Do'), 'DownTown')
        self.assertEqual(htable.read('Ri'), 'Ricardo')
        self.assertEqual(htable.read('Me'), 'Milos')

    def test_delete_method(self):
        htable: hash_table.HashTable = hash_table.HashTable(10)
        htable.create('Do', 'Dot')
        htable.create('Ri', 'Risk')
        htable.create('Me', 'Melancholic')
        htable.delete('Do')
        htable.delete('Ri')
        self.assertEqual(htable.read('Do'), None)
        self.assertEqual(htable.read('Ri'), None)
        self.assertEqual(htable.read('Me'), 'Melancholic')

    def test_full_table(self):
        htable: hash_table.HashTable = hash_table.HashTable(10)
        htable.create('1', 'Do 1')
        htable.create('2', 'Re 1')
        htable.create('3', 'Mi 1')
        htable.create('4', 'Fa')
        htable.create('5', 'Sol')
        htable.create('6', 'Lya')
        htable.create('7', 'Si')
        htable.create('8', 'Do 2')
        htable.create('9', 'Re 2')
        htable.create('banana', 'Mi 2')
        htable.create('kamar', 'BANANA')
        self.assertEqual(htable.read('1'), 'Do 1')
        self.assertEqual(htable.read('2'), 'Re 1')
        self.assertEqual(htable.read('3'), 'Mi 1')
        self.assertEqual(htable.read('4'), 'Fa')
        self.assertEqual(htable.read('5'), 'Sol')

    def test_str_method(self):
        htable: hash_table.HashTable = hash_table.HashTable(10)
        htable.create('1', 'Do 1')
        htable.create('2', 'Re 1')
        htable.create('3', 'Mi 1')
        htable.create('4', 'Fa')
        htable.create('4', 'Fa')
        htable_str = ("1: ('4', 'Fa')\n" + "2: None\n" + "3: None\n" + "4: ('1', 'Do 1')\n" + "5: None\n" +
                      "6: None\n" + "7: ('2', 'Re 1')\n" + "8: None\n" + "9: None\n" + "10: ('3', 'Mi 1')\n")
        self.assertEqual(str(htable), htable_str)


if __name__ == '__main__':
    unittest.main()
