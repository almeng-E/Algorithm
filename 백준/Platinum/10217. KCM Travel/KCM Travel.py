import sys
input = sys.stdin.readline
from collections import deque

INF = float('inf')
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for i in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, d, c))  # nxt, 거리, 가격

    for i in range(1, N+1):
        graph[i].sort(key= lambda x: (x[1], x[2]))


    DP = [[INF for _ in range(M+1)] for _ in range(N+1)]    # DP[노드][가격] = 거리
    for i in range(0, M+1):
        DP[1][i] = 0
    q = deque()
    q.append((1, 0, 0))     # 노드, 비용, 거리

    while q:
        cur, c, d = q.popleft()
        if cur == N:
            continue
        if DP[cur][c] < d:    # 가지치기
            continue

        for nxt, dd, dc in graph[cur]:
            nd = d + dd
            nc = c + dc
            if nc > M:
                continue

            if DP[nxt][nc] > nd:
                for j in range(nc, M+1):
                    if DP[nxt][j] < nd:
                        break
                    DP[nxt][j] = nd
                q.append((nxt, nc, nd))

    res = min(DP[N])

    print(res if res != INF else "Poor KCM")

