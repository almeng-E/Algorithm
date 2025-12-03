import sys
input = sys.stdin.readline

N, M, t = map(int, input().split())

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()


p = [i for i in range(N+1)]


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    rt_a = find(a)
    rt_b = find(b)
    if rt_b != rt_a:
        p[rt_b] = rt_a


v = [False] * (N+1)
v[1] = True

res = 0
cnt = 0
for c, a, b in edges:
    if cnt == N-1:
        break

    if find(a) == find(b):
        continue
    else:
        union(a, b)
        res += c
        res += t*cnt
        cnt += 1

print(res)