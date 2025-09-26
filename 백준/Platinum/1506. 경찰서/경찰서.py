import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())
cost = list(map(int, input().split()))
graph = [list(map(int, input().rstrip())) for _ in range(N)]

def dfs1(cur):
    visited[cur] = True
    for nxt in range(N):
        if graph[cur][nxt] == 0:
            continue
        if not visited[nxt]:
            dfs1(nxt)
    v_order.append(cur)


visited = [False] * N
v_order = []
for i in range(N):
    if not visited[i]:
        dfs1(i)


def dfs2(cur):
    global SCC_ID
    visited[cur] = True
    SCC[cur] = SCC_ID
    for nxt in range(N):
        if graph[nxt][cur] == 0:
            continue
        if not visited[nxt]:
            dfs2(nxt)


visited = [False] * N
SCC_ID = 0
SCC = [-1] * N
for j in reversed(v_order):
    if not visited[j]:
        dfs2(j)
        SCC_ID += 1


lowest = [float('inf')] * SCC_ID
for i in range(N):
    lowest[SCC[i]] = min(lowest[SCC[i]], cost[i])
print(sum(lowest))