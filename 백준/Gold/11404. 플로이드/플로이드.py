import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = float('inf')
# g[a][b] : a->b 금액
g = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a][b] = min(c, g[a][b])

for i in range(N+1):
    g[i][i] = 0

for k in range(N+1):
    for a in range(N+1):
        for b in range(N+1):
            g[a][b] = min(g[a][b], g[a][k] + g[k][b])

for i in range(1, N+1):
    for j in range(1, N+1):
        if g[i][j] == INF:
            g[i][j] = 0
for r in g[1:]:
    print(*r[1:])