import hash_table


def main():
    while True:
        print(htable)
        print('-' * 66)
        print("1. Create value (key, value).")
        print("2. Read value by key (key).")
        print("3. Update value by key (key, value).")
        print("4. Delete value by key (key).")
        print("0. Exit.")
        print("If you enter an invalid input, you will be forwarded to the menu.")
        choice: str = input("Enter you choice: ")
        match choice:
            case "1":
                key, value = input("Key: "), input("Value: ")
                htable.create(key, value)
            case "2":
                key = input("Key: ")
                print("Value:", htable.read(key))
            case "3":
                key, value = input("Key: "), input("Value: ")
                htable.update(key, value)
            case "4":
                key = input("Key: ")
                htable.delete(key)
            case "0":
                exit()
            case _:
                print("Invalid input.")


if __name__ == '__main__':
    htable: hash_table.HashTable = hash_table.HashTable(10)
    main()
