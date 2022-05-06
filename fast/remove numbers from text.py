import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = list(input())
x = ""
for i in s:
    if i.isalpha():
        x = x + i
    elif i == ' ':
        x = x + ' '
print(x)
