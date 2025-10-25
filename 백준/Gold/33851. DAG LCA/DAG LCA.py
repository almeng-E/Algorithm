import sys
input = sys.stdin.readline
from collections import deque


N, M, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
r_graph = [[] for _ in range(N+1)]

INF = float('inf')

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    r_graph[b].append(a)


def bfs(st):
    d = [INF] * (N+1)
    d[st] = 0
    q = deque()
    q.append(st)
    while q:
        c = q.popleft()
        for nxt in r_graph[c]:
            if d[nxt] > d[c]+1:
                d[nxt] = d[c]+1
                q.append(nxt)
    return d


out = []

for _ in range(Q):
    a, b = map(int, input().split())

    da = bfs(a)
    db = bfs(b)

    ans = INF

    for x in range(1, N+1):
        if da[x] != INF and db[x] != INF:
            ans = min(ans, max(da[x], db[x]))

    out.append(str(ans) if ans != INF else '-1')

print('\n'.join(out))