#!/bin/python

import sys


def solve(grades):
    res = []
    for i in grades[1:]:
        if i < 38:
            res.append(i)
        elif (i+1) %5 == 0:
            res.append(i+1)
        elif (i+2) % 5 == 0:
            res.append(i+2)
        else:
            res.append(i)
    return res


# n = int(raw_input().strip())
# grades = []
# grades_i = 0
# for grades_i in xrange(n):
#     grades_t = int(raw_input().strip())
#     grades.append(grades_t)
result = solve([4, 85, 67, 38, 33])
print "\n".join(map(str, result))
