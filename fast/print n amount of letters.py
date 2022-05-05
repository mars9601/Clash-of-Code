n = int(input())

for i in range(n):
    print(*[chr(j+65) for j in range(i+1)], sep='')