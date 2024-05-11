from typing import List
from hash_table.hashing import sha1


class HashTable:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.table: List = [None] * self.size

    def __str__(self) -> str:
        result: str = ""
        i: int = 1
        for info in self.table:
            if info is None:
                result += f"{i}: Пусто\n"
            else:
                result += f"{i}: {info}\n"
            i += 1
        return result

    def _hash(self, key: str) -> int:
        return int(sha1(key.encode()), 16) % self.size

    def _probe(self, index: int, i: int) -> int:
        return (index + i ** 2) % self.size

    def create(self, key: str, value: str) -> None:
        index: int = self._hash(key)
        i: int = 0
        while True:
            probe_index: int = self._probe(index, i)
            if self.table[probe_index] is None:
                self.table[probe_index] = (key, value)
                return
            i += 1

    def read(self, key: str) -> str:
        index: int = self._hash(key)
        i: int = 0
        while True:
            probe_index: int = self._probe(index, i)
            if self.table[probe_index] is None:
                return None
            elif self.table[probe_index][0] == key:
                return self.table[probe_index][1]
            i += 1

    # def read(self, key: str) -> str:
    # """
    # Another version of read func
    # """
    #     index: int = self._hash(key)
    #     read_data: List = []
    #     i: int = 0
    #     while True:
    #         probe_index: int = self._probe(index, i)
    #         if self.table[probe_index] is None:
    #             return read_data
    #         elif self.table[probe_index][0] == key:
    #             read_data.append(self.table[probe_index][1])
    #         elif self.table[probe_index][0] != key:
    #             return read_data
    #         i += 1

    def update(self, key: str, value: str) -> None:
        index: int = self._hash(key)
        i: int = 0
        while True:
            probe_index: int = self._probe(index, i)
            if self.table[probe_index] is None:
                print("Key not found")
                return
            elif self.table[probe_index][0] == key:
                self.table[probe_index] = (key, value)
                return
            i += 1

    def delete(self, key: str) -> None:
        index: int = self._hash(key)
        i: int = 0
        while True:
            probe_index: int = self._probe(index, i)
            if self.table[probe_index] is None:
                print("Key not found")
                return
            elif self.table[probe_index][0] == key:
                self.table[probe_index] = None
                return
            i += 1
