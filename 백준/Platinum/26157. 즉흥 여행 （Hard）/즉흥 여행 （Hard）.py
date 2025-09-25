import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


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


in_degree = [0] * SCC_ID
out_degree = [0] * SCC_ID
for a, b in edges:
    if SCC[a] != SCC[b]:
        in_degree[SCC[b]] += 1
        out_degree[SCC[a]] += 1

in0cnt = 0
out0cnt = 0
src = -1

for i in range(SCC_ID):
    if in_degree[i] == 0:
        src = i
        in0cnt += 1
    if out_degree[i] == 0:
        out0cnt += 1

if in0cnt != 1:
    print(0)
else:
    if out0cnt > 1:
        print(0)
    else:
        res = []
        for i in range(1, N+1):
            if SCC[i] == src:
                res.append(i)
        print(len(res))
        print(*sorted(res))