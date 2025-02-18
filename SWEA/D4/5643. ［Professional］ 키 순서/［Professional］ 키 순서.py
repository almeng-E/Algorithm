def dfs(v, graph):
    visited[v] = True

    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node, graph)


T = int(input())

for TC in range(T):
    # 학생 수
    N = int(input())
    # 키 비교 수
    M = int(input())

    to_parent_graph = [[] for _ in range(N + 1)]
    to_child_graph = [[] for _ in range(N + 1)]

    # 그래프 입력
    for _ in range(M):
        # 키 : a < b
        # 방향 : a -> b
        a, b = map(int, input().split())
        to_parent_graph[a].append(b)
        to_child_graph[b].append(a)

    res = 0

    # dfs 탐색 및 결과 확인
    for node in range(1, N + 1):
        visited = [False] * (N + 1)
        dfs(node, to_parent_graph)
        dfs(node, to_child_graph)
        if sum(visited) == N:
            res += 1

    print(f'#{TC + 1} {res}')