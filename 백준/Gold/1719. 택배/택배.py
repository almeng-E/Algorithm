import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

INF = float('inf')
dist = [[INF for _ in range(N+1)] for _ in range(N+1)]

ans = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    hq = []
    d = dist[i]
    d[i] = 0
    ans[i][i] = '-'
    for f_node, w in g[i]:
        hq.append((w, f_node, f_node))
        d[f_node] = w
        ans[i][f_node] = str(f_node)

    while hq:
        cur_d, cur, f_node = heappop(hq)
        if d[cur] < cur_d:
            continue

        for nxt, w in g[cur]:
            nxt_d = cur_d + w
            if d[nxt] > nxt_d:
                d[nxt] = nxt_d
                ans[i][nxt] = str(f_node)
                heappush(hq, (nxt_d, nxt, f_node))

for i in range(1, N+1):
    print(' '.join(ans[i][1:]))