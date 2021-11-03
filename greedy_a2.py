S = input()
sum = int(S[0])
for i in range(len(S)-1):
    a = int(S[i+1])
    if (sum + a) > (sum * a):
        sum = sum + a
    else:
        sum = sum * a
print(sum)