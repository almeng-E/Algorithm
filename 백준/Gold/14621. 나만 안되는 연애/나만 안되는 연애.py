import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    rt_a = find(a)
    rt_b = find(b)
    if rt_a == rt_b:
        return
    else:
        p[rt_b] = rt_a



N, M = map(int, input().split())
g = [0] + input().split()
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))
edges.sort(key=lambda x: x[2])

p = [i for i in range(N+1)]
vi = [False] * (N+1)
ret = 0
cnt = 0
for u, v, d in edges:
    if find(u) != find(v) and g[u] != g[v]:
        cnt += 1
        ret += d
        union(u, v)
    if cnt == (N-1):
        break
if cnt == (N-1):
    print(ret)
else:
    print(-1)
