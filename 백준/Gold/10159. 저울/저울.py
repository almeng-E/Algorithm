import sys
input = sys.stdin.readline


def dfs(cur, g):
    v[cur] = True
    for nxt in g[cur]:
        if not v[nxt]:
            dfs(nxt, g)

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
r_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    r_graph[b].append(a)

ans = [N] * (N+1)
for i in range(1, N+1):
    v = [False] * (N+1)
    dfs(i, graph)
    v[i] = False
    dfs(i, r_graph)
    ans[i] -= sum(v)
print('\n'.join(map(str, ans[1:])))