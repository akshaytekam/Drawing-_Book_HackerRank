#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    #return min(p//2, n//2 - p//2)            # We can write in one liner as well or the below lengthy logic
    half = math.ceil(n/2)
    if p == 1:
        return 0
    elif p < half:
        pages_To_Turn = math.floor(p/2)
        return pages_To_Turn
    elif p > half:
        pages_To_Flip = (n//2-p//2)
        return pages_To_Flip
    return 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
