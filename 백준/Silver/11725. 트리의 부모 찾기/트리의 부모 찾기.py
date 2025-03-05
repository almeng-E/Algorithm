import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, depth):
    visited[v] = depth

    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node, depth+1)


N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
dfs(1, 1)

for i in range(2, N+1):
    for j in graph[i]:
        if visited[i] > visited[j]:
            print(j)
            break