import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

def f(n):
    r = 0
    for d in range(1, n):
        if n%d==0:
            r += d
    return r

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

dif = n - f(n)
if dif > 0:
    print("deficient")
if dif < 0:
    print("abundant")
if dif == 0:
    print("perfect")