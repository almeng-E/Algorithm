import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
r_graph = [[] for _ in range(N+1)]
edges = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    r_graph[b].append(a)
    edges.append((a, b))


visited = [False] * (N+1)
v_order = []


def dfs1(cur):
    visited[cur] = True
    for nxt in r_graph[cur]:
        if not visited[nxt]:
            dfs1(nxt)
    v_order.append(cur)


for i in range(1, N+1):
    if not visited[i]:
        dfs1(i)

SCC_ID = 0
SCC = [-1] * (N+1)
visited = [False] * (N+1)


def dfs2(cur):
    global SCC_ID
    visited[cur] = True
    SCC[cur] = SCC_ID
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs2(nxt)


for i in reversed(v_order):
    if not visited[i]:
        dfs2(i)
        SCC_ID += 1


in_cnt = [0] * SCC_ID
for a, b in edges:
    if SCC[a] != SCC[b]:
        in_cnt[SCC[b]] += 1

if SCC_ID == 1:
    print('Yes')
else:
    f = 1
    for i in range(SCC_ID):
        if in_cnt[i] == 0:
            f = 0
            break
    if f:
        print('Yes')
    else:
        print('No')