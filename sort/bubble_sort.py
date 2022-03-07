n = int(input())
d = list(map(int, input().split()))
flag = 1
while flag:
    flag = 0
    for i in range(n):
        j = n - 1 - i
        if d[j] < d[j-1]:
            a = d[j]
            d[j] = d[j-1]
            d[j-1] = a
            flag = 1
print(d)