#!/bin/python3

import sys


N = int(input().strip())
y= int(N%2)
if (y==1):
    print ('Weird')
else:
    if N in range(2,5):
        print ('Not Weird')
    elif N in range(6,21):
        print ('Weird')
    elif N in range(21,101):
         print ('Not Weird')