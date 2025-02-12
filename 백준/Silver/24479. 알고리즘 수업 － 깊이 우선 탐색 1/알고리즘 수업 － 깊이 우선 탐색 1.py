import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, visited, v):
    global cnt
    cnt += 1
    visited[v] = cnt
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)




N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

# 그래프 정보 저장
for _ in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

# 그래프 내부 정렬
for i in range(1, N+1):
    graph[i].sort()

# dfs 실행
cnt = 0
dfs(graph, visited, R)


# 출력
for i in range(1, N+1):
    print(visited[i])



