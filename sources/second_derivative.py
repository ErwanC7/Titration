##
# EPITECH PROJECT, 2021
# second_derivative.py
# File description:
# second derivative
##

import sys


def second_rate(array, i, data):
    return (data[i + 1] - data[i]) / (array[i + 1][0] - array[i][0])


def second_deriv(array, first_deriv):
    deriv = []

    print("Second derivative:")
    for i in range(2, len(array) - 2):
        print("%.1f" % array[i][0], "ml -> ", end="")
        if array[i + 1][0] - array[i - 1][0] == 0:
            sys.exit(84)
        a = array[i][0] - array[i - 1][0]
        b = array[i + 1][0] - array[i][0]
        x = second_rate(array, i, first_deriv)
        y = second_rate(array, i - 1, first_deriv)
        if a + b == 0:
            sys.exit(84)
        result = (x * a + y * b) / (a + b)
        print("%.2f" % result)
        deriv.append(result)
    return deriv
