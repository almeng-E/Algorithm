import sys
input = sys.stdin.readline


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    global res, w
    rt_a = find(a)
    rt_b = find(b)
    if rt_a != rt_b:
        res += size[rt_b] * size[rt_a] * w
        p[rt_b] = rt_a
        size[rt_a] += size[rt_b]


N = int(input())
edges = []
for _ in range(N-1):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

p = [i for i in range(N+1)]
size = [1 for _ in range(N+1)]

edges.sort(reverse=True)

res = 0
for w, a, b in edges:
    union(a, b)

print(res)