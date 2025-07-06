import sys
input = sys.stdin.readline


from heapq import heappop, heappush

N, M = map(int, input().split())
oil = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

# 1 --> N
INF = float('inf')
# 그냥 1차원으로 하면 "상태"가 뭉개짐, 특정 금액(최소)일 때 출발을 시켜야함
DP = [dict() for _ in range(N + 1)]

DP[1][oil[1]] = 0
hq = [(0, 1, oil[1])]   # 비용, 위치, 현재까지의 최소 oil 비용

while hq:
    cost, cur, cheapest = heappop(hq)
    if cost > DP[cur].get(cheapest, INF):
        continue

    for nxt, w in graph[cur]:
        n_cost = cost + cheapest * w
        n_cheapest = min(cheapest, oil[nxt])
        if n_cost < DP[nxt].get(n_cheapest, INF):
            DP[nxt][n_cheapest] = n_cost
            heappush(hq, (n_cost, nxt, n_cheapest))

print(min(DP[N].values()))