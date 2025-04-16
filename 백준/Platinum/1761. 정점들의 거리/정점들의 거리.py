import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 높이 구하기, 누적값구하기
depth = [-1] * (N+1)
distance = [0] * (N+1)
parent = [1] * (N+1)

queue = deque()
queue.append(1)
depth[1] = 0
distance[1] = 0
parent[1] = 1

while queue:
    x = queue.popleft()

    for n_node, weight in graph[x]:
        if depth[n_node] == -1:
            depth[n_node] = depth[x] + 1                # 깊이 갱신
            distance[n_node] = distance[x] + weight     # 거리 갱신
            parent[n_node] = x                          # 부모 저장
            queue.append(n_node)



M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    res = distance[a] + distance[b]

    while depth[a] > depth[b]:
        a = parent[a]
    while depth[b] > depth[a]:
        b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]


    res -= (distance[a] * 2)
    print(res)


