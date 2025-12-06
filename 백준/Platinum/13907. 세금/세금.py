import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
S, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
def solve():
    INF = float('inf')
    dp = [[INF for _ in range(N)] for _ in range(N + 1)]  # dp[노드][지나온간선수]

    for j in range(N):
        dp[S][j] = 0
    q = deque()
    q.append((0, 0, S))
    while q:
        dist, cnt, cur = q.popleft()

        if dp[cur][cnt] < dist:
            continue

        if cur == E:
            continue
        if cnt == N - 1:
            continue

        for nxt, w in graph[cur]:
            nd = dist + w
            if dp[nxt][cnt + 1] > nd:
                dp[nxt][cnt + 1] = nd
                q.append((nd, cnt + 1, nxt))

    paths = []
    cur_min = INF
    for i in range(1, N):
        if dp[E][i] != INF and dp[E][i] < cur_min:
            cur_min = dp[E][i]
            paths.append((i, dp[E][i]))

    res = []
    updates = [0]
    for _ in range(K):
        updates.append(int(input()))
    tax = 0
    for u in updates:
        tax += u
        out = INF
        for k, v in paths:
            out = min(out, tax * k + v)
        res.append(str(out))

    print('\n'.join(res))
solve()