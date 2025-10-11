import sys
input = sys.stdin.readline
sys.setrecursionlimit(25000000)

D = int(input())
L = int(input())
graph = [[] for _ in range(D+1)]
r_graph = [[] for _ in range(D+1)]

for _ in range(L):
    a, b = map(int, input().split())
    graph[a].append(b)
    r_graph[b].append(a)


def dfs1(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs1(nxt)
    v_order.append(cur)


visited = [False] * (D+1)
v_order = []
for i in range(1, D+1):
    if not visited[i]:
        dfs1(i)


def dfs2(cur):
    global cnt
    visited[cur] = True
    cnt += 1
    for nxt in r_graph[cur]:
        if not visited[nxt]:
            dfs2(nxt)


res = 0
visited = [False] * (D+1)
for i in reversed(v_order):
    cnt = 0
    if not visited[i]:
        dfs2(i)
    res = max(cnt, res)
print(res)