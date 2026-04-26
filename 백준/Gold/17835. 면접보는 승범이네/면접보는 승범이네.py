import sys
input = sys.stdin.readline

from heapq import heappop, heappush
N, M, K = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[b].append((a, c))

INF = float('inf')
v = [INF] * (N+1)

hq = []
st = list(map(int, input().split()))
for s in st:
    heappush(hq, (0, s))
    v[s] = 0

while hq:
    d, cur = heappop(hq)
    if v[cur] < d:
        continue

    for nxt, w in G[cur]:
        nd = d+w
        if v[nxt] > nd:
            v[nxt] = nd
            heappush(hq, (nd, nxt))

cur_max = -1
ans = 0

for i in range(1, N+1):
    if cur_max < v[i]:
        cur_max = v[i]
        ans = i
print(ans)
print(cur_max)
