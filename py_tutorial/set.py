# 중복x,순서x
a = set()
a = {1,3,5,7,9}
data = set([1,1,2,3,4,4,5])
dat = {1,1,2,3,4,4,5} #위와 동일
print(data)
print(dat)
print(a|dat) #합집합
print(a&dat) #교집합
print(a-dat) #차집합
a.add(4) #추가
a.update([10,11])#여러개 추가
a.remove(3)#삭제