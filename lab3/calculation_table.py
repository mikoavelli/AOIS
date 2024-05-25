from minimization import minimization, beautiful_minimization
from sknf_sdnf import get_sknf_sdnf
from tabulate import tabulate


def calculation_table(minimiz: tuple[tuple[str]], constituents: tuple[tuple[str]], is_sdnf: bool):
    print('SDNF' if is_sdnf else "SKNF")
    minimiz: tuple[tuple[str]] = tuple(tuple(el for el in _list if el != 'X') for _list in minimiz)
    cons: list = beautiful_minimization(constituents, is_sdnf=is_sdnf).split(' 🇻 ') if is_sdnf \
        else beautiful_minimization(constituents, is_sdnf=is_sdnf).split(' ∧ ')
    data = []
    headers: list[str] = [el.strip('()') for el in cons]
    repeating: dict[str: dict] = {}
    for imp in minimiz:
        new_data = [imp]
        repeating[imp] = {}
        for constituent in constituents:
            repeating[imp][constituent] = set(imp).issubset(set(constituent))
            new_data.append(repeating[imp][constituent])
        data.append(new_data)

    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
    implicates_to_remove: set = set()
    data = [[el for el in _list if type(el) is not tuple] for _list in data]
    for i in range(len(data)):
        if is_sdnf:
            total = [_list.count(True) for _list in data]
        else:
            total = [_list.count(False) for _list in data]
        for j in range(len(data[i])):
            if is_sdnf:
                if data[i][j]:
                    for k in range(len(data)):
                        if i == k:
                            continue
                        if data[k][j]:
                            total[k] = total[k] - 1
                            break
            else:
                if not data[i][j]:
                    for k in range(len(data)):
                        if i == k:
                            continue
                        if not data[k][j]:
                            total[k] = total[k] - 1
                            break
        for j in range(len(total)):
            if not total[j]:
                implicates_to_remove.add(i)
    if not implicates_to_remove:
        result = []
        for i in range(len(minimiz)):
            if i not in implicates_to_remove:
                result.append(minimiz[i])
        return tuple(result)
    else:
        return minimiz
