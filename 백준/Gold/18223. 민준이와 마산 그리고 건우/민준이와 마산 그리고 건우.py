from heapq import heappop, heappush
import sys
input = sys.stdin.readline

V, E, P = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

path = [set() for _ in range(V+1)]
dist = [float('inf') for _ in range(V+1)]

dist[1] = 0
hq = []
hq.append((0, 1))

while hq:
    d, cur = heappop(hq)
    if dist[cur] < d:
        continue
    if cur == V:
        break

    for nxt, w in graph[cur]:
        nd = d + w
        if dist[nxt] > nd:
            dist[nxt] = nd
            path[nxt].clear()
            path[nxt].add(cur)
            heappush(hq, (nd, nxt))
        elif dist[nxt] == nd:
            path[nxt].add(cur)
            heappush(hq, (nd, nxt))

# dfs
stack = list(path[V])
visited = [0] * (V+1)
visited[V] = 0
saved = False
while stack:
    cur = stack.pop()
    if cur == P:
        saved = True
        break

    for nxt in path[cur]:
        if not visited[nxt]:
            stack.append(nxt)
            visited[nxt] = 1

if saved:
    print("SAVE HIM")
else:
    print("GOOD BYE")