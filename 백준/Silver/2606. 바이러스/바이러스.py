def dfs(v):
    visited[v] = True

    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node)

# N : 컴퓨터 수
N = int(input())

edges = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(1)

print(sum(visited) - 1)