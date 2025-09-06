import sys
input = sys.stdin.readline


from heapq import heappop, heappush

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))


M, x = map(int, input().split())
macdonalds = set(map(int, input().split()))

S, y = map(int, input().split())
starbucks = set(map(int, input().split()))


# 맥도날드
M_SET = set()
hq = []
dist = [(x+1)] * (V+1)
for mc in macdonalds:
    hq.append((0, mc))
    dist[mc] = 0

while hq:
    d, cur = heappop(hq)
    if dist[cur] < d:
        continue

    for nxt, w in graph[cur]:
        nd = d + w
        if dist[nxt] > nd:
            dist[nxt] = nd
            heappush(hq, (nd, nxt))
            if (nxt not in starbucks) and (nxt not in macdonalds):
                M_SET.add(nxt)


# 스타벅스
S_SET = set()
hq = []
s_dist = [(y+1)] * (V+1)
for st in starbucks:
    hq.append((0, st))
    s_dist[st] = 0

while hq:
    d, cur = heappop(hq)
    if s_dist[cur] < d:
        continue

    for nxt, w in graph[cur]:
        nd = d + w
        if s_dist[nxt] > nd:
            s_dist[nxt] = nd
            heappush(hq, (nd, nxt))

            if (nxt not in starbucks) and (nxt not in macdonalds):
                S_SET.add(nxt)

ret = float('inf')

houses = M_SET & S_SET
for h in houses:
    ret = min(ret, dist[h] + s_dist[h])


print(ret if ret != float('inf') else -1)
