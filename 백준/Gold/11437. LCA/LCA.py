import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 깊이와 부모를 찾자
depth = [-1] * (N+1)
parent = [1] * (N+1)
queue = deque()

depth[1] = 0
queue.append(1)

while queue:
    x = queue.popleft()

    for nx in graph[x]:
        if depth[nx] == -1:
            depth[nx] = depth[x] + 1
            parent[nx] = x
            queue.append(nx)
# LCA
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())

    while depth[a] > depth[b]:
        a = parent[a]

    while depth[a] < depth[b]:
        b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    print(a)