import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    fa = find(a)
    fb = find(b)
    if fa != fb:
        p[fa] = fb


N, Q = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(Q)]
p = [i for i in range(N+1)]

edges.sort(key=lambda x: (x[2], x[3]))

cnt = 0
ret = 0
ret1 = 0
for a, b, c, t in edges:
    if find(a) != find(b):
        union(a, b)
        ret += c
        cnt += 1
        ret1 = max(ret1, t)
    if cnt == N-1:
        print(f'{ret1} {ret}')
        break

else:
    print(-1)