import sys
n = int(sys.stdin.readline())
d = []
for i in range(n):
    d.append(list(map(str, sys.stdin.readline().split())))
    d[i][1] = int(d[i][1])
    d[i][2] = int(d[i][2])
    d[i][3] = int(d[i][3])

d.sort(key= lambda x:x[0])
d.sort(key= lambda x:x[3], reverse=True)
d.sort(key= lambda x:x[2])
d.sort(key= lambda x:x[1], reverse=True)
print("-----------------------------")
for i in range(n):
    print(d[i][0])