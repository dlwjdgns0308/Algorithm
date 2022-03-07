import sys
n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    minj = i
    for j in range(i,n):
        if d[j] < d[i]:
            minj = j
            a = d[i]
            d[i] = d[minj]
            d[minj] = a
print(d)