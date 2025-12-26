import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
t = [0] * (N+1)
g = [[] for _ in range(N+1)]
dp = [0] * (N+1)
in_degree = [0] * (N+1)

for i in range(1, N+1):
    time, *prv, end = map(int, input().split())
    t[i] = time
    in_degree[i] = len(prv)
    for p in prv:
        g[p].append(i)

q = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)
        dp[i] = t[i]

while q:
    cur = q.popleft()
    for nxt in g[cur]:
        in_degree[nxt] -= 1
        if dp[nxt] < dp[cur] + t[nxt]:
            dp[nxt] = dp[cur] + t[nxt]
        if in_degree[nxt] == 0:
            q.append(nxt)

print(*dp[1:], sep='\n')