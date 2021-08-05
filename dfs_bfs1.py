from collections import deque

def bfs(graph, start, visited):

    queue = deque([start])
    print("queue", queue)
    visited[start] = True
    print(visited)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            print("i = ",i)
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9 # false로 초기화
print(visited)

bfs(graph,1,visited)