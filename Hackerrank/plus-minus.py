#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    r = [0,0,0]
    for i in arr:
        if i > 0:
            r[0] += 1
        elif i < 0:
            r[1] += 1
        else:
            r[2] += 1
    print(round(r[0]/n, 6))
    print(round(r[1]/n, 6))
    print(round(r[2]/n, 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)