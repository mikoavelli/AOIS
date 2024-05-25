from copy import deepcopy


def calculation(minimiz: tuple[tuple[str]], is_sdnf: bool):
    list_without_x: list = [[el for el in _list if el != 'X'] for _list in minimiz]
    implicates_to_remove: set = set()
    for i in range(len(list_without_x)):
        elements: dict = {}
        for el in list_without_x[i]:
            if el[0] == '!':
                elements[el] = 1 if is_sdnf else 0
                elements[el[-1]] = 0 if is_sdnf else 1
            else:
                elements[el] = 1 if is_sdnf else 0
                elements['!' + el] = 0 if is_sdnf else 1
        new_list = deepcopy(list_without_x)
        new_list.remove(list_without_x[i])

        for _list in new_list:
            for j in range(len(_list)):
                if _list[j] in elements:
                    _list[j] = elements[_list[j]]

        for _list in new_list.copy():
            for el in _list.copy():
                if el == (1 if is_sdnf else 0):
                    _list.remove(el)

            if not _list:
                implicates_to_remove.add(i)
    if implicates_to_remove:
        for index, implicate in enumerate(list_without_x.copy()):
            if index in implicates_to_remove:
                list_without_x.remove(implicate)
    return list_without_x
