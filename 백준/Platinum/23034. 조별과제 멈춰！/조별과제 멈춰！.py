import sys
input = sys.stdin.readline
from collections import deque


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]



N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])
p = [i for i in range(N + 1)]
cost = 0
cnt = 0

g = [[] for _ in range(N+1)]

for a, b, c in edges:
    if cnt == N - 1:
        break

    rt_a = find(a)
    rt_b = find(b)
    if rt_a != rt_b:
        p[rt_b] = rt_a
        cnt += 1
        cost += c
        g[a].append((b, c))
        g[b].append((a, c))


ans = []
Q = int(input())
for _ in range(Q):
    X, Y = map(int, input().split())
    q = deque()
    q.append((X, 0))
    v = [0] * (N+1)
    v[X] = 1
    while q:
        cur, w_max = q.popleft()
        if cur == Y:
            ans.append(cost - w_max)
            break
        for nxt, w in g[cur]:
            if not v[nxt]:
                v[nxt] = 1
                q.append((nxt, max(w_max, w)))

print('\n'.join(map(str, ans)))
