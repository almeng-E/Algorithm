import heapq
import sys
input = sys.stdin.readline


INF = 987654321
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)


for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

hq = []
distance[X] = 0
heapq.heappush(hq, (0, X)) # 거리, 노드번호

while hq:
    c_dist, c_node = heapq.heappop(hq)

    if distance[c_node] < c_dist: continue

    for next_node in graph[c_node]:
        if distance[next_node] > c_dist + 1:
            distance[next_node] = c_dist + 1
            heapq.heappush(hq, (distance[next_node], next_node))




res = []
for i in range(1, N+1):
    if distance[i] == K:
        res.append(i)

if res:
    for i in res:
        print(i)
else:
    print(-1)