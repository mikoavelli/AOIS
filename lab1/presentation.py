from main import *


def presentation_to_binary() -> None:
    conv_1 = to_binary_direct(12)
    conv_2 = to_binary_direct(-12)
    conv_3 = to_binary_reverse(26)
    conv_4 = to_binary_reverse(-26)
    conv_5 = to_binary_additional(5)
    conv_6 = to_binary_additional(-5)

    print(f"12 to binary direct: {conv_1, from_binary(conv_1, 'd')}")
    print(f"-12 to binary direct: {conv_2, from_binary(conv_2, 'd')}")
    print(f"26 to binary reverse: {conv_3, from_binary(conv_3, 'r')}")
    print(f"-26 to binary reverse: {conv_4, from_binary(conv_4, 'r')}")
    print(f"5 to binary additional: {conv_5, from_binary(conv_5, 'a')}")
    print(f"-5 to binary additional: {conv_6, from_binary(conv_6, 'a')}")

    print("--------------------------------")


def presentation_sum_binary() -> None:
    sum_1 = sum_binary(12, 37)
    sum_2 = sum_binary(12, -37)
    sum_3 = sum_binary(12, -5)
    sum_4 = sum_binary(-12, 37)
    sum_5 = sum_binary(-40, 37)
    sum_6 = sum_binary(-12, -37)

    print(f"Sum 12, 37: {sum_1, from_binary(sum_1, 'a')}")
    print(f"Sum 12, -37: {sum_2, from_binary(sum_2, 'a')}")
    print(f"Sum 12, -5: {sum_3, from_binary(sum_3, 'a')}")
    print(f"Sum -12, 37: {sum_4, from_binary(sum_4, 'a')}")
    print(f"Sum -40, 37: {sum_5, from_binary(sum_5, 'a')}")
    print(f"Sum -12, -37: {sum_6, from_binary(sum_6, 'a')}")

    print("--------------------------------")


def presentation_difference_binary() -> None:
    diff_1 = difference_binary(5, 3)
    diff_2 = difference_binary(5, 9)
    diff_3 = difference_binary(5, -7)
    diff_4 = difference_binary(-12, 37)
    diff_5 = difference_binary(-40, -37)
    diff_6 = difference_binary(-12, -37)

    print(f"Diff 12, 37: {diff_1, from_binary(diff_1, 'a')}")
    print(f"Diff 12, 5: {diff_2, from_binary(diff_2, 'a')}")
    print(f"Diff 12, -5: {diff_3, from_binary(diff_3, 'a')}")
    print(f"Diff -12, 37: {diff_4, from_binary(diff_4, 'a')}")
    print(f"Diff -40, -37: {diff_5, from_binary(diff_5, 'a')}")
    print(f"Diff -12, -37: {diff_6, from_binary(diff_6, 'a')}")

    print("--------------------------------")


def presentation_multiplication() -> None:
    mul_1 = multiplication_binary(12, 5)
    mul_2 = multiplication_binary(12, -5)
    mul_3 = multiplication_binary(-12, 37)
    mul_4 = multiplication_binary(-40, -37)
    mul_5 = multiplication_binary(12, 0)
    mul_6 = multiplication_binary(12, 0)

    print(f"Mult 12, 5: {mul_1, from_binary(mul_1, 'd')}")
    print(f"Mult 12, -5: {mul_2, from_binary(mul_2, 'd')}")
    print(f"Mult -12, 37: {mul_3, from_binary(mul_3, 'd')}")
    print(f"Mult -40, -37: {mul_4, from_binary(mul_4, 'd')}")
    print(f"Mult 12, 0: {mul_5, from_binary(mul_5, 'd')}")
    print(f"Mult -12, 0: {mul_6, from_binary(mul_6, 'd')}")

    print("--------------------------------")


def presentation_division_binary() -> None:
    div_1 = division_binary(24, 8)
    div_2 = division_binary(15, -3)
    div_3 = division_binary(-4, 6)
    div_4 = division_binary(0, 13)
    div_5 = division_binary(-15, -6)
    div_6 = division_binary(14, 8)

    print(f"Division 24 by 8: {div_1, from_binary_float(div_1)}")
    print(f"Division 15 by -3: {div_2, from_binary_float(div_2)}")
    print(f"Division -4 by 6: {div_3, from_binary_float(div_3)}")
    print(f"Division 0 by 13: {div_4, from_binary_float(div_4)}")
    print(f"Division -15 by -6: {div_5, from_binary_float(div_5)}")
    print(f"Division 14 by 8: {div_6, from_binary_float(div_6)}")

    print("--------------------------------")


def presentation_to_binary_float() -> None:
    conv_1 = to_binary_float(0.125)
    conv_2 = to_binary_float(1.0625)
    conv_3 = to_binary_float(12.8)
    conv_4 = to_binary_float(-0.75)
    conv_5 = to_binary_float(-1.875)
    conv_6 = to_binary_float(-15.935)

    print(f"0.125 to binary float: {conv_1, from_binary_float(conv_1)}")
    print(f"1.0625 to binary float: {conv_2, from_binary_float(conv_2)}")
    print(f"12.8 to binary float: {conv_3, from_binary_float(conv_3)}")
    print(f"-0.75 to binary float: {conv_4, from_binary_float(conv_4)}")
    print(f"-1.875 to binary float: {conv_5, from_binary_float(conv_5)}")
    print(f"-15.935 to binary float: {conv_6, from_binary_float(conv_6)}")
    print(f"0 to binary float: {conv_6, from_binary_float(conv_6)}")

    print("--------------------------------")


def presentation_sum_binary_float() -> None:
    sum_1 = sum_binary_float(12.5, 2.125)
    sum_2 = sum_binary_float(3.25, 0)
    sum_3 = sum_binary_float(0.625, 12.25)
    sum_4 = sum_binary_float(0.125, 0.5)
    sum_5 = sum_binary_float(0.375, 0)

    print(f"Sum 12.5 & 2.125: {sum_1, from_binary_float(sum_1)}")
    print(f"Sum 3.25 & 0: {sum_2, from_binary_float(sum_2)}")
    print(f"Sum 0.625 & 12.25: {sum_3, from_binary_float(sum_3)}")
    print(f"Sum 0.125 & 0.5: {sum_4, from_binary_float(sum_4)}")
    print(f"Sum 0.375 & 0: {sum_5, from_binary_float(sum_5)}")

    print("--------------------------------")


def main() -> None:
    presentation_to_binary()
    presentation_sum_binary()
    presentation_difference_binary()
    presentation_multiplication()
    presentation_division_binary()
    presentation_to_binary_float()
    presentation_sum_binary_float()


if __name__ == '__main__':
    main()
