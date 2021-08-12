# 이진탐색 떡볶이 만들기 문제
import sys
def dinary_search(array, target, start, end, hight):

    while start <= end:
        mid = (start + end) //2
        minus = 0
        for i in hight:
            if i-array[mid] >= 0:
                minus += (i-array[mid])

        print("뺀값:", minus)
        # 자른 총합
        # 필요한 떡
        # 둘이 같으면 끝

        if minus == target:
            return array[mid]
        elif minus > target:
            start = mid + 1
        else:
            end = mid - 1

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
hight_array = list(map(int, sys.stdin.readline().rstrip().split(" ")))

#절단기 최대 높이 어레이

array = []
for i in range(max(hight_array)):
    array.append(i)
print(array)
result = dinary_search(array, M, 0, len(array), hight_array)
print(result)