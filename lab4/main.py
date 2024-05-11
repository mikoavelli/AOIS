from minimization_calculation import minimization, first_minimization

first_table = (
    (0, 0, 0, 0, 0),
    (0, 0, 1, 1, 1),
    (0, 1, 0, 1, 1),
    (0, 1, 1, 0, 1),
    (1, 0, 0, 1, 0),
    (1, 0, 1, 0, 0),
    (1, 1, 0, 0, 0),
    (1, 1, 1, 1, 1)
)

second_table = (
    (0, 0, 0, 0, 0, 1, 0, 0),
    (0, 0, 0, 1, 0, 1, 0, 1),
    (0, 0, 1, 0, 0, 1, 1, 0),
    (0, 0, 1, 1, 0, 1, 1, 1),
    (0, 1, 0, 0, 1, 0, 0, 0),
    (0, 1, 0, 1, 1, 0, 0, 1),
    (0, 1, 1, 0, 1, 0, 1, 0),
    (0, 1, 1, 1, 1, 0, 1, 1),
    (1, 0, 0, 0, 1, 1, 0, 0),
    (1, 0, 0, 1, 1, 1, 0, 1)
)


def get_solution_d():
    return tuple(tuple((row[0:3], row[3])) for row in first_table)


def get_solution_v():
    return tuple(tuple((row[0:3], row[4])) for row in first_table)


def get_solution_e():
    return tuple(tuple((row[0:4], row[4])) for row in second_table)


def get_solution_f():
    return tuple(tuple((row[0:4], row[5])) for row in second_table)


def get_solution_g():
    return tuple(tuple((row[0:4], row[6])) for row in second_table)


def get_solution_h():
    return tuple(tuple((row[0:4], row[7])) for row in second_table)


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


def print_table(variables: str, table: tuple[tuple[int]]):
    print(variables)
    for row in table:
        print(*row)


def beautiful_minimization(minimiz: tuple[tuple[str]]):
    res = []
    for i in range(len(minimiz)):
        inner = []
        for j in range(len(minimiz[i])):
            if minimiz[i][j] != 'X':
                inner.append(minimiz[i][j])
        res.append('(' + ' ∧ '.join(inner) + ')')
    return ' 🇻 '.join(res)


def print_minimization_first():
    solution_d = get_solution_d()
    solution_v = get_solution_v()

    sdnf_d: tuple[tuple[str]] = get_sdnf_scnf_forms(solution_d, ('A', 'B', 'P', 'D'))['sdnf']
    sdnf_v: tuple[tuple[str]] = get_sdnf_scnf_forms(solution_v, ('A', 'B', 'P', 'V'))['sdnf']

    minimization_d: str = beautiful_minimization(first_minimization(sdnf_d))
    minimization_v: str = beautiful_minimization(first_minimization(sdnf_v))

    print(f'Sdnf D: {sdnf_d}')
    print(f'Minimization D: {minimization_d}')
    print(f'Sdnf V: {sdnf_v}')
    print(f'Minimization V: {minimization_v}')


def print_minimization_second():
    solution_e = get_solution_e()
    solution_f = get_solution_f()
    solution_g = get_solution_g()
    solution_h = get_solution_h()

    sdnf_e: tuple[tuple[str]] = get_sdnf_scnf_forms(solution_e, ('A', 'B', 'C', 'D', 'E'))['sdnf']
    sdnf_f: tuple[tuple[str]] = get_sdnf_scnf_forms(solution_f, ('A', 'B', 'C', 'D', 'F'))['sdnf']
    sdnf_g: tuple[tuple[str]] = get_sdnf_scnf_forms(solution_g, ('A', 'B', 'C', 'D', 'G'))['sdnf']
    sdnf_h: tuple[tuple[str]] = get_sdnf_scnf_forms(solution_h, ('A', 'B', 'C', 'D', 'H'))['sdnf']

    minimization_e = beautiful_minimization(minimization(sdnf_e))
    minimization_f = beautiful_minimization(minimization(sdnf_f))
    minimization_g = beautiful_minimization(minimization(sdnf_g))
    minimization_h = beautiful_minimization(minimization(sdnf_h))

    print(f'Sdnf E: {sdnf_e}')
    print(f'Minimization E: {minimization_e}')
    print(f'Sdnf F: {sdnf_f}')
    print(f'Minimization F: {minimization_f}')
    print(f'Sdnf G: {sdnf_g}')
    print(f'Minimization G: {minimization_g}')
    print(f'Sdnf H: {sdnf_h}')
    print(f'Minimization H: {minimization_h}')


def first_part_of_code():
    print_table("A B P D V", first_table)
    print_minimization_first()


def second_part_of_code():
    print_table("A B C D E F G H", second_table)
    print_minimization_second()


def main():
    first_part_of_code()
    print('-' * 66)
    second_part_of_code()


if __name__ == '__main__':
    main()
