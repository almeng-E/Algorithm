import sys
input = sys.stdin.readline

from collections import deque


def LCA(a, b):
    while a != b:
        if depth[a] < depth[b]:
            b = p[b]
        elif depth[a] > depth[b]:
            a = p[a]
        else:
            a = p[a]
            b = p[b]
    return a





T = int(input())
for _ in range(T):
    N = int(input())

    graph = [[] for _ in range(N+1)]
    p = [-1 for _ in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        p[b] = a

    a, b = map(int, input().split())

    for i in range(1, N+1):
        if p[i] == -1:
            root = i
            break
    depth = [-1] * (N + 1)
    queue = deque()
    depth[root] = 0
    queue.append(root)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if depth[neighbor] == -1:
                depth[neighbor] = depth[current] + 1
                queue.append(neighbor)

    print(LCA(a, b))