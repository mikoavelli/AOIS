from functools import cache


def is_operator(char: str) -> bool:
    return char in '!|&>~'


def get_priority(char: str) -> int:
    match char:
        case '!':
            return 5
        case '&':
            return 4
        case '|':
            return 3
        case '>':
            return 2
        case '~':
            return 1
        case _:
            return 0


@cache
def infix_to_rpn(expression: str) -> str:
    expression = expression.replace('->', '>')
    output: list[str] = []
    stack: list[str] = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif is_operator(char):
            while stack and is_operator(stack[-1]) and get_priority(stack[-1]) >= get_priority(char):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)


@cache
def solve_rpn_expression(expression: str) -> int:
    stack: list[int] = []
    for char in expression:
        if not is_operator(char):
            stack.append(int(char))
        else:
            if char == '!':
                right = stack.pop()
                stack.append(1 if right == 0 else 0)
            else:
                right = stack.pop()
                left = stack.pop()
                match char:
                    case '&':
                        stack.append(min(left, right))
                    case '|':
                        stack.append(max(left, right))
                    case '>':
                        stack.append(0 if left == 1 and right == 0 else 1)
                    case '~':
                        stack.append(int(left == right))

    return stack.pop()


@cache
def get_variables(expression: str) -> tuple:
    return tuple(sorted(set(ch for ch in expression if ch in 'abcde')))


@cache
def get_solution(expression: str, variables: tuple) -> tuple:
    rpn: str = infix_to_rpn(expression)
    result: list = []

    for num in range(2 ** len(variables)):
        values: tuple = tuple(bin(num)[2:].zfill(len(variables)))
        exp: str = rpn

        for i in range(len(variables)):
            exp = exp.replace(variables[i], values[i])

        values = tuple(map(int, values))
        result.append((values, solve_rpn_expression(exp)))
    return tuple(result)


@cache
def get_scnf_expression(sknf_values: tuple, variables: tuple) -> tuple:
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


@cache
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


@cache
def get_sdnf_sknf_forms(solution: tuple, variables: tuple) -> dict:
    sknf_values: list = []
    sdnf_values: list = []

    for value, result in solution:
        sdnf_values.append(value) if result else sknf_values.append(value)

    return dict(sknf=get_scnf_expression(tuple(sknf_values), variables),
                sdnf=get_sdnf_expression(tuple(sdnf_values), variables))


def get_sknf_sdnf(expression: str) -> dict:
    variables: tuple = get_variables(expression)
    solution: tuple = get_solution(expression, variables)
    return get_sdnf_sknf_forms(solution, variables)
