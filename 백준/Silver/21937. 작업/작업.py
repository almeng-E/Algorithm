import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[b].append(a)

st = int(input())
q = deque()
q.append(st)
v = [0] * (N+1)
while q:
    cur = q.popleft()
    for nxt in g[cur]:
        if not v[nxt]:
            v[nxt] = 1
            q.append(nxt)

print(sum(v))