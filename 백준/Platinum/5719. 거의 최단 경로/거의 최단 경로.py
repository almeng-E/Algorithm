import sys
input = sys.stdin.readline
from heapq import heappush, heappop
from collections import deque

INF = float('inf')
while True:
    N, M = map(int, input().split())
    if N == 0:
        break

    S, D = map(int, input().split())

    graph = [dict() for _ in range(N)]

    for _ in range(M):
        u, v, p = map(int, input().split())
        graph[u][v] = p


    b_node = [[] for _ in range(N)]
    dist = [INF for _ in range(N)]

    dist[S] = 0
    hq = []
    hq.append((0, S))
    while hq:
        d, cur = heappop(hq)
        if cur == D:
            break

        if dist[cur] < d:
            continue

        for nxt, w in graph[cur].items():
            nd = d + w
            if dist[nxt] > nd:
                dist[nxt] = nd
                b_node[nxt] = [cur]
                heappush(hq, (nd, nxt))
            elif dist[nxt] == nd:
                b_node[nxt].append(cur)

    q = deque()
    BAN = set()
    for bef in b_node[D]:
        q.append((bef, D))

    while q:
        cur, nxt = q.popleft()
        if (cur, nxt) in BAN:
            continue
        BAN.add((cur, nxt))
        for bef in b_node[cur]:
            q.append((bef, cur))

    dist = [INF for _ in range(N)]
    dist[S] = 0
    hq = []
    hq.append((0, S))
    while hq:
        d, cur = heappop(hq)
        if cur == D:
            break

        if dist[cur] < d:
            continue

        for nxt, w in graph[cur].items():
            if (cur, nxt) in BAN:
                continue
            nd = d + w
            if dist[nxt] > nd:
                dist[nxt] = nd
                heappush(hq, (nd, nxt))
    if dist[D] == INF:
        print(-1)
    else:
        print(dist[D])
