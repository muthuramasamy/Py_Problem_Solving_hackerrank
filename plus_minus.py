#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    a,b,c=0,0,0
    for i in range (0,n):
        if arr[i] > 0:
            a+=1
        elif arr[i] < 0:
            b+=1
        else:
            c+=1
    print(a/len(arr))
    print(b/len(arr))
    print(c/len(arr))
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
