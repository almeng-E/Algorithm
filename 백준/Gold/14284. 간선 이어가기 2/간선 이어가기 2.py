from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
INF = float('inf')
dist = [[INF, INF] for _ in range(N+1)] # D / P

S, T = map(int, input().split())
dist[S] = [0, 0]
hq = []
hq.append((0, 0, S))

while hq:
    d, p, cur = heappop(hq)
    if dist[cur][0] < d:
        continue

    if dist[cur][0] == d and dist[cur][1] < p:
        continue

    for nxt, w in graph[cur]:
        nd = d+w
        np = p+1

        if dist[nxt][0] > nd:
            dist[nxt] = [nd, np]
            heappush(hq, (nd, np, nxt))
        elif dist[nxt][0] == nd and dist[nxt][1] > np:
            dist[nxt][1] = np
            heappush(hq, (nd, np, nxt))

print(dist[T][0])
