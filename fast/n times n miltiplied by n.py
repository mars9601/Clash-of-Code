import sys
import math

# e.g. n = 5 prints "40" ~~ 5*5+5*4+5*3+5*2+5*1

n = int(input())

r=0
for x in range(n+1):
    r+= n*x
print(r)