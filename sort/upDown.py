n = int(input())
num=[]
result =[]
for i in range(0,n):
    num.append(int(input()))

num.sort(reverse=True)

for i in num:
    print(i, end=" ")
