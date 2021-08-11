import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) //2
        # 찾았을 때
        if array[mid] == target:
            return mid;
        # 타겟이 중간값 왼쪽에 있을 때
        elif array[mid] > target:
            end = mid -1;
        # 타겟이 중간값 오른쪽에 있을 때
        else:
            start = mid +1;

    return None;

N = int(sys.stdin.readline().rstrip())
N_array = list(map(int, input().split()))

M = int(sys.stdin.readline().rstrip())
M_array = list(map(int, input().split()))

N_array.sort()
M_array.sort()
for i in M_array:
    if binary_search(N_array, i, 0, N-1) == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")