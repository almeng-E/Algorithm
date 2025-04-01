import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(x, g):
    visited[x]=True
    for n_x in g[x]:
        if not visited[n_x]:
            dfs(n_x, g)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
r_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    r_graph[b].append(a)
res = 0
for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, graph)
    visited[i]=False
    dfs(i, r_graph)
    
    if sum(visited) == N:
        res += 1

print(res)



