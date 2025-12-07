import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
p = [0] + list(map(int, input().split()))
for i in range(2, N+1):
    graph[p[i]].append(i)

p[1] = 0


def dfs(cur, bef):
    in_order.append(cur)
    for nxt in graph[cur]:
        if nxt == bef:
            continue
        else:
            dfs(nxt, cur)


in_order = []
dfs(1, 0)

dp = [0] * (N+1)
for _ in range(M):
    i, w = map(int, input().split())
    dp[i] += w

for i in in_order:
    dp[i] += dp[p[i]]

print(*dp[1:])