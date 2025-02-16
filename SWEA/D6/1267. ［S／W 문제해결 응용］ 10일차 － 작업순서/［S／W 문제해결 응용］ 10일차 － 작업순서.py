def dfs(v):
    # graph, visited, in_degree --> result
    visited[v] = True
    result.append(v)
    for next_node in graph[v]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0 and not visited[next_node]:
            dfs(next_node)

T = 10
for TC in range(T):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))

    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    # 진입 차수
    in_degree = [0 for _ in range(V+1)]
    # 그래프 저장
    for i in range(0, 2*E, 2):
        graph[edges[i]].append(edges[i+1])
        in_degree[edges[i+1]] += 1

    result = []
    # dfs
    for node in range(1, V+1):
        if in_degree[node] == 0 and not visited[node]:
            dfs(node)

    print(f'#{TC+1}', *result)