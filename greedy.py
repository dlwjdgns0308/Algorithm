import sys
count = 0
n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
d.sort()
for i in range(n):
    a = d[i]
    if d[i] == d[i+a-1]:
            count += 1
print(count)
