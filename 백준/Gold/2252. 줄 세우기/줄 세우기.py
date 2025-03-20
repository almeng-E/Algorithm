import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def dfs(v):
    visited[v] = True

    for nx in graph[v]:
        if not visited[nx]:
            dfs(nx)

    res.append(v)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

res = []

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)

print(*reversed(res))