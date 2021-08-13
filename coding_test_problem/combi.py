from itertools import combinations
import sys

N = int(sys.stdin.readline())
S = []  # 신맛 곱연산
B = []  # 쓴맛 합연산
for i in range(N):
    s, b = map(int, input().split(" "))
    S.append(s)
    B.append(b)

arr= []
for i in range(1, N):
    arr.append(list(combinations(S, i)))

h= list(arr[0][0])
j= list(arr[0][1])
print(arr[0])

# items = ['A', 'B', 'C', 'D']
#
# for i in range(1, len(items)):
#     print(list(map(''.join, combinations(items, i)))) # 조합을 만들려는 아이템과 조합의 수를 반드시넘겨줘야한다.

