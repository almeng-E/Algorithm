import sys
input = sys.stdin.readline


from heapq import heappop, heappush


N, M, K = map(int, input().split())
e = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
v = [False] * (N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

res = 0
hq = []
for i in e:
    v[i] = True
    for nxt, weight in graph[i]:
        heappush(hq, (weight, nxt))

while hq:
    weight, to = heappop(hq)
    if v[to]:
        continue
    v[to] = True
    res += weight
    for nxt, nw in graph[to]:
        if v[nxt]:
            continue
        heappush(hq, (nw, nxt))

print(res)