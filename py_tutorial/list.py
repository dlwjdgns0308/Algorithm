arr1 = [i for i in range(10)] #0~9까지의 리스트
arr2 = [i for i in range(20) if i % 2 == 0] # 짝수 리스트
arr3 = [i * i for i in range(10)] #제곱수 리스트
# 이러한 리스트 컴프리헨션은 2차원리스트를 초기화할때 유용하다
arr4 = [[0]*4 for _ in range(3)]
print(arr4)