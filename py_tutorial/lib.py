#순열
from itertools import permutations

data = ['A','B','C']

result = list(permutations(data, 3)) #모든 순열 구하기
print(result)

#조합
from itertools import combinations

result2 = list(combinations(data,2)) #2개를 뽑는 모든 조합 구하기
print(result2)

#중복순열
from itertools import product
result3 = list(product(data, repeat=2)) # 2개를 뽑는 모든순열(중복o)
print(result3)

#중복조합
from itertools import combinations_with_replacement
result4 = list(combinations_with_replacement(data,2)) #2개를 뽑는 모든조합(중복o)
print(result4)

#등장횟수 계산
from collections import Counter

counter = Counter(['red','red','green','blue','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

#최대공약수,최소공배수
import math

#최소공배수를 구하는 함수
def lcm(a,b):
    return a * b // math.gcd(a,b)
a = 21
b = 14

print(math.gcd(21,14))#최대공약수
print(lcm(21,14)) #최소공배수