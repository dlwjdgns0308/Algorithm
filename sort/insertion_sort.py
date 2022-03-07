import sys
a,b = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
d = []
result = []
for i in range(n):
    d.append(int(sys.stdin.readline()))
if a > b:
    result.append(a-b)
else:
    result.append(b-a)
for i in range(n):
    if d[i] > b:
        result.append(d[i]-b+1)
    else:
        result.append(b-d[i]+1)
print(min(result))