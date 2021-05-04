##
# EPITECH PROJECT, 2021
# main
# File description:
# main of 109titration
##

import sys


def rate(array, i):
    return (array[i + 1][1] - array[i][1]) / (array[i + 1][0] - array[i][0])


def estimation(array, derive):
    estimate = 0.0
    result = 0.0
    pos = 0

    for i in range(1, len(array) - 1):
        if estimate < derive[i]:
            estimate = derive[i]
            result = array[i][0]
            pos = i
    print("\nEquivalence point at %.1f" % result, "ml", end="\n\n")
    return pos


def derivative(array):
    deriv = [0]

    print("Derivative:")
    for i in range(1, len(array) - 1):
        print("%.1f" % array[i][0], "ml -> ", end="")
        if array[i + 1][0] - array[i - 1][0] == 0:
            sys.exit(84)
        a = array[i][0] - array[i - 1][0]
        b = array[i + 1][0] - array[i][0]
        if a + b == 0:
            sys.exit(84)
        result = (rate(array, i) * a + rate(array, i - 1) * b) / (a + b)
        print("%.2f" % result)
        deriv.append(result)
    deriv.append(0)
    return deriv
