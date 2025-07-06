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

# N --> 1 거꾸로
INF = float('inf')
DP = [(INF, INF) for _ in range(N+1)]  # 총 비용, 총 거리

hq = []
hq.append((0, 0, N))    # 비용, 총 이동거리, 노드번호
DP[N] = (0, 0)

while hq:
    c_cost, c_dist, cur = heappop(hq)

    # 유효한가?
    if DP[cur] != (c_cost, c_dist):
        continue

    for nxt, weight in graph[cur]:
        n_dist = c_dist + weight

        n_cost = min(n_dist * oil[nxt], c_cost + oil[nxt] * weight)

        if DP[nxt] > (n_cost, n_dist):
            DP[nxt] = (n_cost, n_dist)
            heappush(hq, (n_cost, n_dist, nxt))

print(DP[1][0])