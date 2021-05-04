##
# EPITECH PROJECT, 2021
# more_derivative.py
# File description:
# second derivative estimation
##
import sys
from math import fabs


def more_rate(array, i, data):
    return (data[i + 1] - data[i]) / (array[i + 1][0] - array[i][0])


def get_gap(nbr_1, nbr_2):
    i = 0
    while nbr_1 < nbr_2:
        nbr_1 += 0.10
        i += 1
    return i - 1


def more_deriv(array, deriv, estim):
    first = [float(array[estim - 1][0]), float(deriv[estim - 3])]
    mid = [float(array[estim][0]), float(deriv[estim - 2])]
    last = [float(array[estim + 1][0]), float(deriv[estim - 1])]
    ml = float(array[estim - 1][0])
    result = first[1]
    try:
        coef_1 = (mid[1] - first[1]) / get_gap(first[0], mid[0])
        coef_2 = (last[1] - mid[1]) / get_gap(mid[0], last[0])
    except ZeroDivisionError:
        sys.exit(0)
    equivalence = first[0]
    ml_equivalence = 0

    print("\nSecond derivative estimated:")
    print("%.1f" % first[0], "ml -> %.2f" % first[1])
    while ml < mid[0] - 0.10:
        ml += 0.10
        result += coef_1
        if fabs(equivalence) > fabs(result):
            equivalence = result
            ml_equivalence = ml
        print("%.1f" % ml, "ml -> %.2f" % result)
    result = mid[1]
    while ml < last[0] - 0.10:
        ml += 0.10
        result += coef_2
        if fabs(equivalence) > fabs(result):
            equivalence = result
            ml_equivalence = ml
        print("%.1f" % ml, "ml -> %.2f" % result)
    print("\nEquivalence point at %.1f ml" % ml_equivalence)
