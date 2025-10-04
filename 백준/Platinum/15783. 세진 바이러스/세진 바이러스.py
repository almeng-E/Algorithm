import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs1(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs1(nxt)
    v_order.append(cur)


visited = [False] * N
v_order = []

for i in range(N):
    if not visited[i]:
        dfs1(i)

def dfs2(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs2(nxt)


visited = [False] * N
cnt = 0
for i in reversed(v_order):
    if not visited[i]:
        dfs2(i)
        cnt += 1

print(cnt)