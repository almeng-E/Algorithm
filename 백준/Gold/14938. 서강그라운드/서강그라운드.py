import heapq
import sys
input = sys.stdin.readline


def djikstra(v):
    hq = [(0, v)]   # 현재 거리, 노드
    distance_dp[v][v] = 0

    while hq:
        q_dist, q_node = heapq.heappop(hq)

        if distance_dp[v][q_node] < q_dist: continue

        for next_path in graph[q_node]:
            next_node, weight = next_path

            if distance_dp[v][next_node] > q_dist + weight:
                distance_dp[v][next_node] = q_dist + weight
                heapq.heappush(hq, (distance_dp[v][next_node], next_node))


INF = float('inf')
N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
node_item = [0] + list(map(int, input().split()))

for _ in range(R):
    A, B, I = map(int, input().split())
    graph[A].append((B, I))  # 다음 노드, 가중치
    graph[B].append((A, I))

distance_dp = [[INF for _ in range(N+1)] for _ in range(N+1)]

# 다익스트라
for i in range(1, N+1):
    djikstra(i)


# 결과 찾기
res = 0
for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        if distance_dp[i][j] <= M:
            tmp += node_item[j]
    res = max(res, tmp)

print(res)