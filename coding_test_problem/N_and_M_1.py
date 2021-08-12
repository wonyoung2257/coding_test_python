# 수열
#입력 N: M:
#1부터 N까지 자연수 중 중복 없이 M개를 고른 수열

N, M = map(int, input().split(" "))
visited = [False] * N
print(visited)
out = []

def solve(depth, N, M):
    if depth == M:
        # 출력
        print(" ".join(map(str, out)))
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] =True
            out.append(i+1)
            solve(depth+1, N, M)
            visited[i] = False
            out.pop()

solve(0, N, M)