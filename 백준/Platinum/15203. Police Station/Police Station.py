import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs1(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs1(nxt)
    v_order.append(cur)


def dfs2(cur):
    global SCC_id
    visited[cur] = True
    SCC[cur] = SCC_id
    for nxt in r_graph[cur]:
        if not visited[nxt]:
            dfs2(nxt)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
r_graph = [[] for _ in range(N+1)]
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    r_graph[b].append(a)
    edges.append((a, b))


v_order = []
visited = [False] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        dfs1(i)

SCC = [-1] * (N+1)
SCC_id = 0
visited = [False] * (N+1)
for i in reversed(v_order):
    if not visited[i]:
        dfs2(i)
        SCC_id += 1

in_ = [0] * SCC_id

for a, b in edges:
    if SCC[a] != SCC[b]:
        in_[SCC[b]] += 1

root = []
for i in range(len(in_)):
    if in_[i] == 0:
        root.append(i)

if len(root) != 1:
    print(0)
else:
    r = root[0]
    res = []
    for i in range(1, N+1):
        if SCC[i] == r:
            res.append(i)
    print(len(res))
    print(*res)