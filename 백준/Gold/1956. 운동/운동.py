import sys
input = sys.stdin.readline

V, E = map(int, input().split())
INF = float('inf')
g = [[INF for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    g[a][b] = min(g[a][b], c)

for i in range(V+1):
    g[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            g[i][j] = min(g[i][j], g[i][k]+g[k][j])

ans = INF
for i in range(1, V+1):
    for j in range(i+1, V+1):
        if i==j: continue
        ans = min(ans, g[i][j] + g[j][i])

print(ans if ans != INF else -1)
