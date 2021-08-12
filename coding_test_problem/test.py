N, M = map(int, input().split())

# N 크기의 방문 array
# dfs 알고리즘으로 풀이
# 깊이가 m과 같아질 때 저장된 array를 형식에 맞게 출력
visited = [False] * N
array =[]

def dfs(depth):
    # 같을 때
    if depth == M:
        print(" ".join(map(str,array)))
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            array.append(i+1)
            dfs(depth +1)
            visited[i] = False
            array.pop()

dfs(0)