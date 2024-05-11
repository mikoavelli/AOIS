def get_variables(sknf: tuple[tuple]):
    return [el[-1] for el in sknf[0]]


def is_subset(tot_1: tuple[tuple[str]], tot_2: tuple[tuple[str]]):
    tot_1 = [el for el in tot_1 if el != 'X']
    tot_2 = [el for el in tot_2 if el != 'X']
    return set(tot_1).issubset(set(tot_2))


def get_tuple_of_tuples(tot: tuple[tuple]) -> tuple[tuple]:
    return tuple(tuple(el) for el in tot)


def get_max_x_count(tot: tuple[tuple]) -> int:
    x = 0
    for el in tot:
        x = max(x, el.count('X'))
    return x


def check_tuple(tot_1: tuple[tuple], tot_2: tuple[tuple]) -> bool:
    if len(tot_1) != len(tot_2):
        return False

    if ('X' in tot_1 and 'X' not in tot_2) or ('X' not in tot_1 and 'X' in tot_2):
        return False

    for i in range(len(tot_1)):
        if (tot_1[i] == 'X' and tot_2[i] != 'X') or (tot_1[i] != 'X' and tot_2[i] == 'X'):
            return False

    diff = 0
    for i in range(len(tot_1)):
        if tot_1[i] != tot_2[i]:
            diff += 1
    if diff != 1:
        return False

    return True


def minimization(sdnf: tuple[tuple[tuple]]):
    minimized = first_minimization(sdnf)
    if len(minimized) == 1:
        return minimized
    while True:
        old_data = minimized
        minimized = other_minimizations(minimized)
        if old_data == minimized:
            break
    return minimized


def other_minimizations(minimized: tuple[tuple]):
    if get_max_x_count(minimized) == len(minimized[0]) - 1:
        return minimized
    result = list()
    for i in range(len(minimized) - 1):
        total = 0
        for j in range(len(minimized)):
            if minimized[i] == minimized[j]:
                continue
            if not check_tuple(minimized[i], minimized[j]):
                total += 1
                continue
            else:
                total = 0
                implicates = []
                for el in range(len(minimized[i])):
                    if minimized[i][el] == minimized[j][el]:
                        implicates.append(minimized[i][el])
                    else:
                        implicates.append('X')
                if tuple(implicates) not in result:
                    result.append(tuple(implicates))
        if len(minimized) != 2 and total == len(minimized) - 1:
            result.append(minimized[i])

    for tup in minimized:
        for imp in result.copy():
            if is_subset(imp, tup):
                break
        else:
            result.append(tup)

    if len(result) == 0:
        return minimized
    return tuple(sorted(set(get_tuple_of_tuples(result))))


def first_minimization(sdnf: tuple[tuple]):
    implicates: list = []
    for i in range(len(sdnf) - 1):
        for j in range(i + 1, len(sdnf)):
            uniq_element = []
            for el in range(len(sdnf[i])):
                if sdnf[i][el] == sdnf[j][el]:
                    uniq_element.append(sdnf[j][el])
            if len(uniq_element) == len(sdnf[0]) - 1:
                implicates.append(uniq_element)

    for tup in sdnf:
        for imp in implicates.copy():
            if set(imp).issubset(set(tup)):
                break
        else:
            implicates.append(tup)

    variables: list = get_variables(sdnf)
    for i in range(len(implicates)):
        for j in range(len(variables)):
            if len(implicates[i]) == len(sdnf[0]):
                continue
            if variables[j] not in implicates[i] and ('!' + variables[j]) not in implicates[i]:
                implicates[i].insert(j, 'X')

    return tuple(sorted(set(get_tuple_of_tuples(implicates))))
