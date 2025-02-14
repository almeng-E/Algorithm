def dfs(v):
    if visited[v]:
       return
    else:
        route.append(v)
        visited[v] = True
        for next_node in graph[v]:
            if not visited[next_node]:
                dfs(next_node)



for _ in range(10):
    TC, E = map(int, input().split())

    graph = [[] for _ in range(100)]   # 0 ~ 99
    visited = [0] * 100
    route = []

    edges = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        graph[edges[i]].append(edges[i+1])

    dfs(0)
    if 99 in route:
        print(f'#{TC} 1')
    else:
        print(f'#{TC} 0')