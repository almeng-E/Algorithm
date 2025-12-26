import sys
input = sys.stdin.readline

N = int(input())
t = [0] * (N+1)
g = [[] for _ in range(N+1)]
dp = [0] * (N+1)
s_nodes = []

for i in range(1, N+1):
    time, *prv, end = map(int, input().split())
    t[i] = time
    for p in prv:
        g[p].append(i)
    if not prv:
        s_nodes.append(i)


def dfs(cur):
    for nxt in g[cur]:
        if dp[nxt] < dp[cur] + t[nxt]:
            dp[nxt] = dp[cur] + t[nxt]
            dfs(nxt)


for s in s_nodes:
    dp[s] = t[s]

for s in s_nodes:
    dfs(s)

for ret in dp[1:]:
    print(ret)