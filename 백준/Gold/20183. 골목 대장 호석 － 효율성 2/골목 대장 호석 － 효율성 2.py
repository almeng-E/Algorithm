import sys
input = sys.stdin.readline

from heapq import heappop, heappush


N, M, A, B, C = map(int, input().split())

g = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

INF = float('inf')
l, r = 1, 10**9
ans = INF
while l <= r:
    mid = (l+r) >> 1

    dist = [INF] * (N+1)
    hq = []
    dist[A] = 0
    hq.append((0, A))
    while hq:
        c_money, cur = heappop(hq)
        if cur == B:
            break
        if dist[cur] < c_money:
            continue
        for nxt, w in g[cur]:
            if w > mid:
                continue
            n_money = c_money + w
            if n_money <= C and dist[nxt] > n_money:
                dist[nxt] = n_money
                heappush(hq, (n_money, nxt))
    if dist[B] <= C:
        ans = min(ans, mid)
        r = mid - 1
    else:
        l = mid + 1

print(ans if ans != INF else -1)