import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

code = input().split('|')

for x in code:
    z=sum(map(int,x.split(',')))
    z%=26
    print(end=chr(ord('a')+z-1))