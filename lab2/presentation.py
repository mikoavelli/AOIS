from main import do_all_operations


def example1() -> None:
    exp: dict = do_all_operations("(a | b) & !c",
                                  get_sdnf_scnf=True,
                                  get_index_numeric=True)
    print(exp['sknf'])
    print(exp['sdnf'])
    print(exp['numeric'])
    print(exp['index'])
    print('-' * 66)


def example2() -> None:
    exp: dict = do_all_operations("!((!a) & (b & (a | c)))",
                                  get_sdnf_scnf=True,
                                  get_index_numeric=True)
    print(exp['sknf'])
    print(exp['sdnf'])
    print(exp['numeric'])
    print(exp['index'])
    print('-' * 66)


def example3() -> None:
    exp: dict = do_all_operations("(((a->b)&(c->d))&((!a)|(d)))->((!a)|(!c))",
                                  get_sdnf_scnf=True,
                                  get_index_numeric=True)
    print(exp['sknf'])
    print(exp['sdnf'])
    print(exp['numeric'])
    print(exp['index'])
    print('-' * 66)


def main() -> None:
    example1()
    example2()
    example3()


if __name__ == '__main__':
    main()
