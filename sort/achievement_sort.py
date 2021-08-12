N = int(input())

array = []
for i in range(0, N):
    name, point = input().split()
    array.append([name, int(point)])

print(array)
result = sorted(array, key= lambda x:x[1])

for i in range(N):
    print(result[i][0], end= ' ')