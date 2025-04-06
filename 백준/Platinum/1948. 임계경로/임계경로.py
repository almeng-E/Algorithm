import sys
input = sys.stdin.readline

def find(x, graph, in_degree):
    queue = deque()
    dist = [-1] * (N + 1)

    queue.append(x)
    dist[x] = 0
    while queue:
        c_node = queue.popleft()

        for n_node, weight in graph[c_node]:
            if dist[n_node] < dist[c_node] + weight:
                dist[n_node] = dist[c_node] + weight
            in_degree[n_node] -= 1

            if in_degree[n_node] == 0:
                queue.append(n_node)
    return dist

from collections import deque

INF = float('inf')

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
r_graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)
r_in_degree = [0] * (N+1)
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    in_degree[b] += 1
    r_graph[b].append((a, w))
    r_in_degree[a] += 1


S, E = map(int ,input().split())

StoE_dist = find(S, graph, in_degree)
EtoS_dist = find(E, r_graph, r_in_degree)

res01 = StoE_dist[E]

res02 = 0
for u in range(1, N+1):
    for v, weight in graph[u]:
        if StoE_dist[u]!= -1 and EtoS_dist[v] != -1 and (StoE_dist[u] + weight + EtoS_dist[v] == res01):
            res02 += 1

print(res01)
print(res02)