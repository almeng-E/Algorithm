import sys
input = sys.stdin.readline

from collections import deque


N, M, A, B = map(int, input().split())

graph = [[] for _ in range(N+1)]

cost = [[]]
for c_idx in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, c_idx))
    graph[v].append((u, c_idx))
    cost[0].append(t)

K = int(input())
for _ in range(K):
    cost.append(list(map(int, input().split())))

q = deque()
# DP[node][magic]
DP = [[float('inf') for _ in range(K+1)] for _ in range(N+1)]
DP[A][0] = 0
q.append((A, 0))
while q:
    cur, m_cnt = q.popleft()
    if cur == B:
        continue
    if m_cnt < K and DP[cur][m_cnt+1] > DP[cur][m_cnt]:
        DP[cur][m_cnt+1] = DP[cur][m_cnt]
        q.append((cur, m_cnt+1))

    for nxt, c_idx in graph[cur]:
        # 현재층
        if DP[nxt][m_cnt] > DP[cur][m_cnt] + cost[m_cnt][c_idx]:
            DP[nxt][m_cnt] = DP[cur][m_cnt] + cost[m_cnt][c_idx]
            q.append((nxt, m_cnt))

print(min(DP[B][i] for i in range(K+1)))
