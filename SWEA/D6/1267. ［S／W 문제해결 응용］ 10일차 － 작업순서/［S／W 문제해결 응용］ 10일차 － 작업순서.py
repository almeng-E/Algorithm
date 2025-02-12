# 조금 더 느린  ?? 코드 ??
# must_visited 탐색 회수가 훨씬 많아 더 느릴 것으로 예상됨


def dfs(graph, visited, current_node):
    global must_precede, res
    # 방문 처리 전, 체크하기    <<< 차이점
    for i in must_precede[current_node]:
        if not visited[i]:
            return
    # 방문 및 재귀 호출
    res.append(current_node)
    visited[current_node] = 1
    # 재귀
    for next_node in graph[current_node]:
        if not visited[next_node]:
            dfs(graph, visited, next_node)



for TC in range(10):
    V, E = map(int, input().split())

    edge_input = list(map(int, input().split()))

    graph = [[] for _ in range(V+1)]
    visited = [1] + [0 for _ in range(V+1)]
    must_precede = [[] for _ in range(V+1)]
    res = []
    # 그래프 정보 입력(방향 o)
    # 선행 정보 입력(거꾸로)
    for i in range(0, len(edge_input), 2):
        graph[edge_input[i]].append(edge_input[i+1])
        must_precede[edge_input[i+1]].append(edge_input[i])

    while True:
        if sum(visited) == V+1:
            break

        for node in range(1, V+1):
            if not visited[node]:
                dfs(graph, visited, node)

    print(f'#{TC+1} ', end="")
    print(*res)
