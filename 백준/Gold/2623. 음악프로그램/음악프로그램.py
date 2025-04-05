import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [set() for _ in range(N+1)]
in_degree = [0] * (N+1)

# 그래프 입력
for _ in range(M):
    x, *arr = map(int, input().split())
    for i in range(x-1):
        if arr[i+1] not in graph[arr[i]]:
            graph[arr[i]].add(arr[i+1])
            in_degree[arr[i+1]] += 1

# topological sort
path = []
queue = deque()
for i in range(1, N+1):
    if not in_degree[i]:
        queue.append(i)
if queue:
    cycle = False
else:
    cycle = True


while queue and not cycle:
    c_node = queue.popleft()

    path.append(c_node)

    for n_node in graph[c_node]:
        in_degree[n_node] -= 1
        if in_degree[n_node] < 0:
            cycle = True
            break

        elif in_degree[n_node] == 0:
            queue.append(n_node)

if cycle or len(path) != N:
    print(0)
else:
    for node in path:
        print(node)
