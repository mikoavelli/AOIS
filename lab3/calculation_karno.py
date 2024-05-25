from sknf_sdnf import get_solution, get_variables
from tabulate import tabulate
from minimization import minimization, beautiful_minimization
from sknf_sdnf import get_sknf_sdnf, get_sdnf_sknf_forms


def karno_2(values) -> None:
    headings: list[str] = ['0', '1']
    strings: list[str] = ['0', '1']
    result: list[list[str]] = [[strings[i]] for i in range(len(strings))]

    for i in range(len(strings)):
        for j in range(len(headings)):
            result[i].append(values[len(headings) * i + j])

    print(tabulate(result, headers=headings, tablefmt="fancy_grid"))


def karno_3(values) -> None:
    headings: list[str] = ['00', '01', '11', '10']
    strings: list[str] = ['0', '1']
    result: list[list[str]] = [[strings[i]] for i in range(len(strings))]

    for i in range(len(strings)):
        for j in range(len(headings)):
            result[i].append(values[len(headings) * i + [0, 1, 3, 2][j]])

    print(tabulate(result, headers=headings, tablefmt="fancy_grid"))


def karno_4(values) -> None:
    headings: list[str] = ['00', '01', '11', '10']
    strings: list[str] = ['00', '01', '11', '10']
    result: list[list[str]] = [[strings[i]] for i in range(len(strings))]

    for i in range(len(strings)):
        for j in range(len(headings)):
            result[[0, 1, 3, 2][i]].append(values[len(headings) * i + [0, 1, 3, 2][j]])

    print(tabulate(result, headers=headings, tablefmt="fancy_grid"))


def karno_5(values) -> None:
    headings: list[str] = ['000', '001', '011', '010', '110', '111', '101', '100']
    strings: list[str] = ['00', '01', '11', '10']
    result: list[list[str]] = [[strings[i]] for i in range(len(strings))]

    for i in range(len(strings)):
        for j in range(len(headings)):
            result[[0, 1, 3, 2][i]].append(values[len(headings) * i + [0, 1, 3, 2, 6, 7, 5, 4][j]])

    print(tabulate(result, headers=headings, tablefmt="fancy_grid"))


def main(expression: str) -> dict | None:
    values = [row[1] for row in get_solution(expression, get_variables(expression))]
    result_sknf: tuple = []
    result_sdnf: tuple = []
    sknf = get_sknf_sdnf(expression)['sknf']
    sdnf = get_sknf_sdnf(expression)['sdnf']
    match (len(values)):
        case 4:
            karno_2(values)
            result_sknf = minimization(sknf)
            result_sdnf = minimization(sdnf)
        case 8:
            karno_3(values)
            result_sknf = minimization(sknf)
            result_sdnf = minimization(sdnf)
        case 16:
            karno_4(values)
            result_sknf = minimization(sknf)
            result_sdnf = minimization(sdnf)
        case 32:
            karno_5(values)
            result_sknf = minimization(sknf)
            result_sdnf = minimization(sdnf)
    if result_sdnf:
        return {'sknf': result_sknf, 'sdnf': result_sdnf}
    return None
