import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))     # 도착노드, 가중치

S, E = map(int, input().split())

# 다익스트라

# 초기 작업
INF = 987654321
distance = [INF] * (N+1)
path = [[] for _ in range(N+1)]
distance[S] = 0
path[S] = [S]

hq = []
heapq.heappush(hq, (0, S)) # 거리, 노드

while hq:
    q_dist, q_node = heapq.heappop(hq)

    # 현재 큐의 시작 노드값으로 갱신 진행하면 안됨
    if distance[q_node] < q_dist: continue

    for next_path in graph[q_node]:
        next_node, weight = next_path

        # 주위 체크
        if distance[next_node] > q_dist + weight:
            distance[next_node] = q_dist + weight
            heapq.heappush(hq, (distance[next_node], next_node))
            path[next_node] = path[q_node] + [next_node]

print(distance[E])
print(len(path[E]))
print(*path[E])