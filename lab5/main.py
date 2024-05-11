from minimization_calculation import minimization

table = (
    (1, 0, 0, 0, 0, 0, 1, 0, 0, 1),
    (1, 0, 0, 1, 0, 1, 0, 0, 1, 1),
    (1, 0, 1, 0, 0, 1, 1, 0, 0, 1),
    (1, 0, 1, 1, 1, 0, 0, 1, 1, 1),
    (1, 1, 0, 0, 1, 0, 1, 0, 0, 1),
    (1, 1, 0, 1, 1, 1, 0, 0, 1, 1),
    (1, 1, 1, 0, 1, 1, 1, 0, 0, 1),
    (1, 1, 1, 1, 0, 0, 0, 1, 1, 1)
)


def get_solution_1():
    return tuple([((row[0], row[3], row[2], row[1]), row[-1]) for row in table])


def get_solution_2():
    return tuple([((row[0], row[3], row[2], row[1]), row[-2]) for row in table])


def get_solution_3():
    return tuple([((row[0], row[3], row[2], row[1]), row[-3]) for row in table])


def get_sknf_expression(sknf_values: tuple, variables: tuple) -> tuple:
    result: list = []
    for values in sknf_values:
        temp: list = []
        for i in range(len(values)):
            if values[i] != 0:
                temp.append('!' + variables[i])
            else:
                temp.append(variables[i])
        result.append(tuple(temp))
    return tuple(result)


def get_sdnf_expression(sdnf_values: tuple, variables: tuple) -> tuple:
    result: list = []
    for values in sdnf_values:
        temp: list = []
        for i in range(len(values)):
            if values[i] != 1:
                temp.append('!' + variables[i])
            else:
                temp.append(variables[i])
        result.append(tuple(temp))
    return tuple(result)


def get_sdnf_scnf_forms(solution: tuple, variables: tuple) -> dict:
    sknf_values: list = []
    sdnf_values: list = []

    for value, result in solution:
        sdnf_values.append(value) if result else sknf_values.append(value)

    return dict(sknf=get_sknf_expression(tuple(sknf_values), variables),
                sdnf=get_sdnf_expression(tuple(sdnf_values), variables))


def beautiful_minimization(minimiz: tuple[tuple[str]]):
    res = []
    for i in range(len(minimiz)):
        inner = []
        for j in range(len(minimiz[i])):
            if minimiz[i][j] != 'X':
                inner.append(minimiz[i][j])
        res.append('(' + ' ∧ '.join(inner) + ')')
    return ' 🇻 '.join(res)


def print_table():
    variables: list[str] = 'V A* B* C* A B C H1 H2 H3'.split()
    for col in range(len(table[0])):
        print(variables[col].rjust(3), end=' ')
        for row in range(len(table)):
            print(table[7 - row][col], end=' ')
        print()


def print_minimization():
    solution_1 = get_solution_1()
    solution_2 = get_solution_2()
    solution_3 = get_solution_3()

    sdnf_1 = get_sdnf_scnf_forms(solution_1, ('V', 'A', 'B', 'C', 'H1'))['sdnf']
    sdnf_2 = get_sdnf_scnf_forms(solution_2, ('V', 'A', 'B', 'C', 'H2'))['sdnf']
    sdnf_3 = get_sdnf_scnf_forms(solution_3, ('V', 'A', 'B', 'C', 'H3'))['sdnf']

    minimization_1 = beautiful_minimization(minimization(sdnf_1))
    minimization_2 = beautiful_minimization(minimization(sdnf_2))
    minimization_3 = beautiful_minimization(minimization(sdnf_3))

    print(f'Sdnf 1: {sdnf_1}')
    print(f'Minimization 1: {minimization_1}')
    print(f'Sdnf 2: {sdnf_2}')
    print(f'Minimization 2: {minimization_2}')
    print(f'Sdnf 3: {sdnf_3}')
    print(f'Minimization 3: {minimization_3}')


def main():
    print_table()
    print_minimization()


if __name__ == '__main__':
    main()
