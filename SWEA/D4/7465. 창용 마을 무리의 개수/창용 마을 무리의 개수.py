def dfs(v):

    visited[v] = True
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node)


T = int(input())
for TC in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    cnt = 0
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            dfs(i)
    print(f'#{TC+1} {cnt}')