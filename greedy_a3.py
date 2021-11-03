n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
while True:
    b = int(a[0])
    if len(a) < b:
        break
    elif b < int(a[1]):
        b = int(a[1])
    for j in range(b):
        if len(a) == 0:
            break
        del a[0]
    count = count + 1
print(count)

