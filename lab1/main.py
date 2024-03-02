NUMBER_OF_BINARY_DIGITS: int = 16


def to_binary(num: int, number_of_binary_digits: int = NUMBER_OF_BINARY_DIGITS) -> str:
    local_num: int = num
    result: str = ''

    while local_num > 0:
        result = str(local_num % 2) + result
        local_num //= 2

    return result.zfill(number_of_binary_digits)


def to_binary_direct(num: int, number_of_binary_digits: int = NUMBER_OF_BINARY_DIGITS) -> str:
    if num >= 0:
        return to_binary(num, number_of_binary_digits)
    return '1' + to_binary(abs(num), number_of_binary_digits)[1:]


def to_binary_reverse(num: int, number_of_binary_digits: int = NUMBER_OF_BINARY_DIGITS) -> str:
    binary_num: str = to_binary(abs(num), number_of_binary_digits)

    if num >= 0:
        return binary_num

    result: str = ''
    for el in binary_num:
        result += '1' if el == '0' else '0'
    return result


def to_binary_additional(num: int, number_of_binary_digits: int = NUMBER_OF_BINARY_DIGITS) -> str:
    binary_num: str = to_binary_reverse(num, number_of_binary_digits)

    if num >= 0:
        return binary_num

    result: str = ''
    add_term: int = 1

    for el in binary_num[::-1]:
        current_sum: int = add_term + int(el)
        if current_sum >= 2:
            add_term = 1
            result += '0'
        else:
            add_term = 0
            result += str(current_sum)

    return result[::-1]


def from_binary(num: str, code: str) -> int:
    if num[0] == '1' and (code == 'a' or code == 'r'):
        binary: str = num if code == 'r' else sum_binary(num, -1, len(num))
        result = num[0]
        for i in range(1, len(binary)):
            result += '1' if binary[i] == '0' else '0'
    else:
        result = num
    total: int = 0
    for i in range(-1, -len(result), -1):
        total += int(result[i]) * 2 ** (abs(i) - 1)

    return total * (-1 if num[0] == '1' else 1)


def sum_binary(num_1, num_2, number_of_binary_digits: int = NUMBER_OF_BINARY_DIGITS) -> str:
    binary_1: str = to_binary_additional(num_1, number_of_binary_digits) if type(num_1) is int else num_1
    binary_2: str = to_binary_additional(num_2, number_of_binary_digits) if type(num_2) is int else num_2

    binary_1, binary_2 = binary_1[::-1], binary_2[::-1]

    result: str = ''
    add_term: int = 0

    for i in range(len(binary_1)):
        current_sum: int = add_term + int(binary_1[i]) + int(binary_2[i])
        if current_sum >= 2:
            add_term = 1
            result += str(current_sum - 2)
        else:
            add_term = 0
            result += str(current_sum)

    return result[::-1]


def difference_binary(num_1: int, num_2: int, number_of_binary_digits: int = NUMBER_OF_BINARY_DIGITS) -> str:
    return sum_binary(num_1, abs(num_2) if num_2 < 0 else -num_2, number_of_binary_digits)


def multiplication_binary(num_1: int, num_2: int, number_of_binary_digits: int = NUMBER_OF_BINARY_DIGITS) -> str:
    sign: str = '1' if num_1 * num_2 < 0 else '0'
    binary_1: str = to_binary_direct(num_1, number_of_binary_digits)[::-1]
    binary_2: str = to_binary_direct(num_2, number_of_binary_digits)[::-1]
    result: str = '0' * number_of_binary_digits

    for i in range(len(binary_2)):
        if binary_2[i] == '0':
            continue
        temp: str = '0' * i + binary_1[:number_of_binary_digits - i]
        result = sum_binary(result, temp[::-1], number_of_binary_digits)

    return sign + result[1:]


def div_helper(num_1: int, num_2: int) -> str:
    dividend: str = to_binary_direct(abs(num_1)).lstrip('0')
    divisor: str = to_binary_direct(abs(num_2)).lstrip('0')
    quotient: str = ''

    current_dividend: str = ''
    for digit in dividend:
        current_dividend += digit
        if from_binary(current_dividend, 'd') >= from_binary(dividend, 'd'):
            times: int = from_binary('0' + current_dividend, 'd') // from_binary('0' + divisor, 'd')
            quotient += str(times)
            current_dividend = to_binary(
                from_binary('0' + current_dividend, 'd') - from_binary('0' + divisor, 'd') * times)
        else:
            quotient += '0'

    return quotient


def division_binary(num_1: int, num_2: int) -> str:
    if num_2 == 0:
        raise ValueError
    sign: str = '1' if num_1 * num_2 < 0 else '0'

    whole: str = div_helper(abs(num_1), abs(num_2))
    fractional: str = '0'
    if num_1 % num_2 != 0:
        fractional = div_helper((abs(num_1) % abs(num_2)) * 10 ** 5, abs(num_2))

    whole = str(from_binary(sign + whole, 'd'))
    fractional = str(from_binary(fractional, 'd')).rstrip('0')
    result: float = float(whole + '.' + fractional)

    return to_binary_float(result)


def get_sign_whole_fractional(num: float) -> tuple[str, str, str]:
    local_num: float = abs(num)
    sign: str = '0' if num >= 0 else '1'
    whole: str = to_binary(int(local_num))
    fractional_part: float = local_num - int(local_num)

    fractional: str = ''
    for i in range(23):
        fractional_part *= 2
        if fractional_part >= 1:
            fractional += '1'
            fractional_part -= 1
        else:
            fractional += '0'

    return sign, whole, fractional


def to_binary_float(num: float) -> str:
    sign, whole, fractional = get_sign_whole_fractional(num)

    if '1' in whole:
        order: int = len(whole[whole.index('1'):]) - 1
        if order == 0:
            return sign + to_binary(127, 8) + fractional
        mantis: str = whole[len(whole) - order:] + fractional[:-order]
        return sign + to_binary(order + 127, 8) + mantis
    elif '1' in fractional:
        order = -(len(fractional[:fractional.index('1')]) + 1)
        mantis = fractional[abs(order):] + '0' * abs(order)
        return sign + to_binary(order + 127, 8) + mantis
    else:
        return '0' * 32


def from_binary_float(num: str) -> float:
    sign, order_str, mantis = num[0], '0' + num[1:9], num[9:]
    order: int = from_binary(order_str, 'd') - 127

    if order > 0:
        whole: int = from_binary('01' + mantis[:order], 'd')
        mantis = mantis[order:].rstrip('0')
    elif order < 0:
        whole = 0
        mantis = ('0' * abs(order + 1) + '1' + mantis[:order]).rstrip('0')
    else:
        whole = 1
        mantis = mantis.rstrip('0')

    fractional: float = 0
    for i in range(len(mantis)):
        fractional += int(mantis[i]) * 2 ** (-(i + 1))

    return (1 - 2 * int(sign)) * (whole + fractional)


def sum_binary_float(num_1: float, num_2: float) -> str:
    binary_1: str = to_binary_float(num_1)
    binary_2: str = to_binary_float(num_2)

    order_1: int = from_binary('0' + binary_1[1:9], 'd') - 127
    order_2: int = from_binary('0' + binary_2[1:9], 'd') - 127

    mantis_1: str = '001' + binary_1[9:]
    mantis_2: str = '001' + binary_2[9:]

    if (order_diff := order_1 - order_2) < 0:
        mantis_1 = mantis_1[0] + abs(order_diff) * '0' + mantis_1[1:-abs(order_diff)]
    elif order_diff > 0:
        mantis_2 = mantis_2[0] + abs(order_diff) * '0' + mantis_2[1:-abs(order_diff)]

    mantis_sum: str = sum_binary(mantis_1, mantis_2)
    return '0' + to_binary(max(order_1, order_2) + 127, 8) + mantis_sum[3:]
