import sys
input = sys.stdin.readline


from heapq import heappop, heappush

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

sight = list(map(int, input().split()))

dist = [float('inf')] * N

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

hq = []
hq.append((0, 0))
dist[0] = 0

while hq:
    d, cur = heappop(hq)
    if dist[cur] < d:
        continue

    for nxt, w in graph[cur]:
        if sight[nxt] and nxt != N-1:
            continue

        nd = d + w
        if dist[nxt] > nd:
            dist[nxt] = nd
            heappush(hq, (nd, nxt))
res = dist[N-1]
if res != float('inf'):
    print(res)
else:
    print(-1)







