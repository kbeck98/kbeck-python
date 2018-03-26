#!/bin/python3

import os
import sys

# create reversed array, print values and return 
def reverseArray(a):
    rev=[]
    for i in range(len(a)-1, -1, -1):
        print(a[i])
        rev.append(a[i])  
    return rev
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
