# e.g. "ACDEGFH" it prints "F"
w = list(input())
for i in range(len(w) - 1):
    if w[i] > w[i + 1]:
        print(w[i+1])
