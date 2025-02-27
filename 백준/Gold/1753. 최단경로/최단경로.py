import heapq
import sys
input=sys.stdin.readline

INF = 987654321

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# 다익스트라
# 초기화 작업
hq = []
#
# distance[K] = 0
# for next_path in graph[K]:
#     n_node, weight = next_path
#     distance[n_node] = weight
#     heapq.heappush(hq, (distance[n_node], n_node))
distance[K] = 0
heapq.heappush(hq, (distance[K], K))

while hq:
    c_dist, c_node = heapq.heappop(hq)

    if distance[c_node] < c_dist: continue # 이미 갱신됨

    for next_path in graph[c_node]:
        n_node, weight = next_path

        if distance[n_node] > c_dist + weight:
            distance[n_node] = c_dist + weight
            heapq.heappush(hq, (distance[n_node], n_node))

# 실행 완료
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])