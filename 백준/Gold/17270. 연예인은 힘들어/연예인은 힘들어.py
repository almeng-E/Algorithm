import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())

g = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

dist = [[float('inf'), float('inf')] for _ in range(N+1)]

J, S = map(int, input().split())

hq = []
heappush(hq, (0, J, 0))
heappush(hq, (0, S, 1))
dist[J][0] = 0
dist[S][1] = 0

while hq:
    d, cur, person = heappop(hq)

    if dist[cur][person] < d:
        continue

    for nxt, w in g[cur]:
        nd = d + w
        if dist[nxt][person] > nd:
            dist[nxt][person] = nd
            heappush(hq, (nd, nxt, person))

dist[J][1] = float('inf')
dist[S][0] = float('inf')

min_dist = min(map(sum, dist))
j_min_dist = float('inf')
ans = -1

for i in range(1, N+1):
    if sum(dist[i]) != min_dist:
        continue
    if i == J or i == S:
        continue

    if dist[i][0] > dist[i][1]:
        continue

    if j_min_dist > dist[i][0]:
        j_min_dist = dist[i][0]
        ans = i
print(ans)