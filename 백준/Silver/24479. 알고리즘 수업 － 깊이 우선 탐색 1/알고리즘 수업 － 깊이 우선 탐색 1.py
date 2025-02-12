def dfs_stack(graph, start):
    visited = [0 for _ in range(N + 1)]
    stack = [start]
    cnt = 0
    while stack:
        v = stack.pop()
        if not visited[v]:
            cnt += 1
            visited[v] = cnt
            for next_node in reversed(graph[v]):
                if not visited[next_node]:
                    stack.append(next_node)

    return visited

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

# 그래프 정보 저장 (양방향)
for _ in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

# 그래프 내부 정렬
for i in range(1, N+1):
    graph[i].sort()

# dfs 실행
visited = dfs_stack(graph, R)


# 출력
for i in range(1, N+1):
    print(visited[i])



