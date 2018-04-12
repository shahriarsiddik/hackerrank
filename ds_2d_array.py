#!/bin/python3

import os
import sys

def array2D(arr):
    res = None
    for row in range(len(arr)-2):
        first,second,third = arr[row], arr[row+1], arr[row+2]
        for i in range(len(first)-2):
            sm1 = first[i] + first[i+1] + first[i+2]
            sm2 = second[i+1]
            sm3 = third[i] + third[i+1] + third[i+2]
            sum = sm1 + sm2 + sm3
            if res is None:
                res = sum
            else:
                if res<sum:
                    res = sum
    print(res)

array2D([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 9, 2, -4, -4, 0], [0, 0, 0, -2, 0, 0], [0, 0, -1, -2, -4, 0]])
