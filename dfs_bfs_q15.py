from collections import deque

# n: 도시 수, m: 도로의 수, k: 거리 정보, x: 출발 도시 번호
n, m , k, x = map(int, input().split())

graph = [[] for _ in range(n+1)] #??
print(graph)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # ( 1, 2) (1, 3) -> graph[1] = [2,3]


# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
print(q)
while q:
    now = q.popleft()
    print(type(now))
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check =True

if check == False:
    print(-1)