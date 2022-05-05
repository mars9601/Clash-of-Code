import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

drink = input()
straw = int(input())

if straw == 0:
    s = "_________\n"
else:
    s = "____|____\n"
print(s+"\       /\n"+" \  "+drink+"  /\n"+"  \___/")