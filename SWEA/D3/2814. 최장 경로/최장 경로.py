def dfs(v, c_dist):
    global res

    if res < c_dist:
        res = c_dist

    for next_node in graph[v]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, c_dist+1)
            visited[next_node] = False



T = int(input())
for TC in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    res = 0

    for node in range(1, N+1):
        if not visited[node]:
            visited[node] = True
            dfs(node, 1)
            visited[node] = False

    print(f'#{TC+1} {res}')