s=list(input())
x=0
for i in s:
 if i not in list("AEIOUYaeiouy"):
  x=x+ord(i)
print(x)

#shorter
print(sum([ord(c),0][c in'AEIOUYaeiouy']for c in input()))