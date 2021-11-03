n,k = map(int, input().split())
a = []
count = 0
for i in range(n):
    b = int(input())
    a.append(b)
a.reverse()
for j in range(len(a)):
    c = (k // a[j]) * a[j]
    count += (k // a[j])
    k -= c
    
print(count)
