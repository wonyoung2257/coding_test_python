N = int(input())

array = []
for i in range(0, N):
    name, point = input().split()
    array.append([name, int(point)])

def setting(data):
    return data[1]


result = sorted(array, key=setting)

for i in range(N):
    print(result[i][0], end= ' ')