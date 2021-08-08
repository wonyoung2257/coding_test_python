N, K = map(int, input().split())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA.sort()
arrayB.sort(reverse=True)

for i in range(K):
    if arrayA[i] < arrayB[i]:
        arrayA[i] = arrayB[i]
    else:
        break

print(sum(arrayA))