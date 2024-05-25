from calculation import calculation
from calculation_table import calculation_table
from calculation_karno import main as karno
from minimization import beautiful_minimization, minimization
from sknf_sdnf import get_sknf_sdnf


def calc(expression) -> None:
    sknf = get_sknf_sdnf(expression)['sknf']
    sdnf = get_sknf_sdnf(expression)['sdnf']
    minimization_sknf = minimization(sknf)
    minimization_sdnf = minimization(sdnf)
    calculation_sknf = calculation(minimization_sknf, False)
    calculation_sdnf = calculation(minimization_sdnf, True)
    print('Sknf:', sknf)
    print('Sdnf:', sdnf)
    print('Minimization Sknf:', beautiful_minimization(minimization_sknf))
    print('Minimization Sdnf:', beautiful_minimization(minimization_sdnf))
    print('Calculation Sknf:', beautiful_minimization(calculation_sknf))
    print('Calculation Sdnf:', beautiful_minimization(calculation_sdnf))
    print('-' * 66)


def calc_table(expression) -> None:
    sknf = get_sknf_sdnf(expression)['sknf']
    sdnf = get_sknf_sdnf(expression)['sdnf']
    minimization_sknf = minimization(sknf)
    minimization_sdnf = minimization(sdnf)
    calculation_sdnf = calculation_table(minimization_sdnf, sdnf, True)
    calculation_sknf = calculation_table(minimization_sknf, sknf, False)
    print('Sknf:', sknf)
    print('Sdnf:', sdnf)
    print('Minimization Sknf:', beautiful_minimization(minimization_sknf))
    print('Minimization Sdnf:', beautiful_minimization(minimization_sdnf))
    print('Calculation Sknf:', beautiful_minimization(calculation_sknf))
    print('Calculation Sdnf:', beautiful_minimization(calculation_sdnf))
    print('-' * 66)


def calc_karno(expression) -> None:
    sknf = get_sknf_sdnf(expression)['sknf']
    sdnf = get_sknf_sdnf(expression)['sdnf']
    print('Sknf:', sknf)
    print('Sdnf:', sdnf)
    print('Karno Sknf:', beautiful_minimization(karno(expression)['sknf']))
    print('Karno Sdnf:', beautiful_minimization(karno(expression)['sdnf']))


def main():
    expression: str = '(a -> b) & !c & (d ~ e)'
    calc(expression)
    calc_table(expression)
    calc_karno(expression)


if __name__ == '__main__':
    main()
