#이진 탐색(반복문) 코드
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start +end) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result ==None:
    print("원소 없음")
else:
    print(result +1)