#!/bin/python3

import sys


def print_consecutive_ones(inp):
    bin_val = bin(inp)[2:]
    list_break = max(bin_val.split('0'))
    print(len(list_break))


n = int(input().strip())
for i in range(n):
    print_consecutive_ones(i)

