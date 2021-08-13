#N까지의 자연수 M개의 수열 중복없이
#dfs로 풀고 중복되는 값 제거를 어떻게 할지 관건인듯

N, M = map(int, input().split())
visited = [False] * N
result = []

def dfs(depth):
    #깊이와 M이 같다며 출력
    if depth == M:
        print(" ".join(map(str, result)))
        return

    for i in range(len(visited)):
        if not visited[i]:
            #방문으로 기록
            visited[i] = True
            result.append(i+1)
            dfs(depth+1)
            visited[i] = False
            result.pop()



dfs(0)
