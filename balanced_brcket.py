#balanced bracket
import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack=[]
    table={")":"(","]":"[","}":"{"}
    for i in s:
        if i in table and stack and table[i]==stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if stack:
        return("NO")
    else:
        return("YES")
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
