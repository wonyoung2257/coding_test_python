#N개의 재료 신맛 S 쓴맛 B
#신맛은 재료의 곱 쓴맛은 합
#신맛과 쓴맛의 차이가 가장 적은 요리
import sys

N = int(sys.stdin.readline())

S = []  # 신맛 곱연산
B = []  # 쓴맛 합연산
temp12 = 1e9 # 파이썬 최대값

for i in range(N):
    s, b = map(int, input().split(" "))
    S.append(s)
    B.append(b)

def combi(num, s, b):
    global temp12
    if num == N:
        if s == 1 and b == 0:
            return
        if temp12 > abs(s-b):
            temp12 = abs(s-b)
        return

    combi(num+1, S[num]*s, B[num]+b)
    combi(num+1, s, b)

combi(0,1,0)
print(temp12)