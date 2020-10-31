"""
Alphabet Rangoli

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/pythonist3/challenges/alphabet-rangoli

import string


def print_rangoli(size):
    width = size * 2 - 2
    center = width
    grid = []
    row = ['-'] * (width * 2 + 1)
    for i in range(size + 1):
        for j in range(i):
            row[center - j * 2] = string.ascii_lowercase[size + j - i]
            row[center + j * 2] = string.ascii_lowercase[size + j - i]
        grid.append(''.join(row))
    for x in grid[1:] + grid[-2:0:-1]:
        print(x)
