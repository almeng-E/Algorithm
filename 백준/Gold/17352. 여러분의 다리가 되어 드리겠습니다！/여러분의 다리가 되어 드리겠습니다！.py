import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
g = [[] for _ in range(N+1)]
for _ in range(N-2):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def dfs(cur):
    for nxt in g[cur]:
        if not v[nxt]:
            v[nxt] = True
            dfs(nxt)


res = []
v = [False] * (N+1)
for i in range(1, N+1):
    if not v[i]:
        v[i] = True
        dfs(i)
        res.append(i)
print(*res)