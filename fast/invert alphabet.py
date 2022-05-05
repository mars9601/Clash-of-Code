import sys
import math
import string
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = list(input())

x = list(string.ascii_uppercase)
y = list(string.ascii_uppercase)
y.sort(reverse=True)
z = ""
for i in l:
    index = x.index(i)
    z = z + y[index]
print(z[::-1])


