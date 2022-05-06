import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a={}
q=""
x = input()
for i in x:
    if i not in a:
        a[i]=1
    else: a[i]+=1
    q+=i*a[i]
    


print(q)
