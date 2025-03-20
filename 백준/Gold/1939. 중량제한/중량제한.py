import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(v, current_min):
    if v == y:
        return current_min
    for n_node, dist in graph[v]:
        if not visited[n_node]:
            visited[n_node] = True
            # 현재 경로에서의 최소값은 지금까지의 current_min과 현재 간선의 dist 중 더 작은 값
            candidate = dfs(n_node, min(current_min, dist))
            if candidate != -1:  # 도착점 y에 도달한 경우
                return candidate
    return -1  # y에 도달하지 못한 경우

# 크루스칼
def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])
    return p[x]

def union_set(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)
    if root_a == root_b:
        return
    else:
        p[root_b] = root_a


N, M = map(int, input().split())
p = [i for i in range(N+1)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2], reverse=True)

e_cnt = 0
res = float('inf')

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# MST 찾기
for a, b, c in edges:
    if find_parent(a) == find_parent(b):
        continue
    else:
        union_set(a, b)
        e_cnt += 1
        graph[a].append((b, c))
        graph[b].append((a, c))

    if e_cnt == N-1:
        break

x, y = map(int, input().split())
visited = [False] * (N+1)
visited[x] = True
answer = dfs(x, float('inf'))
print(answer)

