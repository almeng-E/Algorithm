import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline



def 깊이우선탐색(v):
    for n_node, weight in graph[v]:
        if visited[n_node] == -1:
            visited[n_node] = visited[v] + weight
            깊이우선탐색(n_node)


INF = float('inf')
V = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(V):
    node, *info, _ = map(int, input().split())

    for i in range(0, len(info), 2):
        graph[node].append((info[i], info[i+1]))    # 인접 노드, 가중치


visited = [-1] * (V+1)
visited[1] = 0
깊이우선탐색(1)
tmp = 0
idx = 0
for i in range(1, V+1):
    if tmp < visited[i]:
        tmp = visited[i]
        idx = i


visited = [-1] * (V+1)
visited[idx] = 0
깊이우선탐색(idx)
res = max(visited)
print(res)