#!/usr/bin/env python3
##
# EPITECH PROJECT, 2021
# main
# File description:
# main of 109titration
##

import sys
import csv
import os

from sources.first_derivative import derivative, estimation
from sources.second_derivative import second_deriv
from sources.more_derivative import more_deriv


def filled_up(reader, arr):
    i = 0

    for row in reader:
        arr.append([])
        for j in range(2):
            try:
                if i > 0 and j == 0 and float(row[j]) == arr[i - 1][0]:
                    return False
                if float(row[j]) < 0:
                    return False
                arr[i].append(float(row[j]))
            except ValueError:
                return False
        i += 1
    return arr


def openning(filepath):
    arr = []

    try:
        if os.stat(filepath).st_size < 4:
            return False
    except IOError:
        return False
    with open(filepath) as csvFile:
        reader = csv.reader(csvFile, delimiter=';')
        arr = filled_up(reader, arr)
        if not arr:
            return False
    csvFile.close()
    return arr


def main(ac, av):
    if ac != 2:
        return 84
    array = openning(av[1])
    if not array:
        return 84
    deriv = derivative(array)
    estim = estimation(array, deriv)
    if estim < 3 or estim + 2 > len(array):
        return 0
    more_deriv(array, second_deriv(array, deriv), estim)
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
