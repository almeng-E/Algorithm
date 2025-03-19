# DFS 풀이
def dfs(v):
    global cnt
    visited[v] = True
    for n_node in graph[v]:
        if not visited[n_node]:
            dfs(n_node)


T = int(input())

for TC in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for node in range(1, N+1):
        if not visited[node]:
            dfs(node)
            cnt += 1

    print(f'#{TC+1} {cnt}')