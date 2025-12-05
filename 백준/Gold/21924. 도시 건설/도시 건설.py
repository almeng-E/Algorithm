import sys
input = sys.stdin.readline


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    rta = find(a)
    rtb = find(b)
    if rta != rtb:
        p[rtb] = rta


N, M = map(int, input().split())
p = [i for i in range(N+1)]
edges = []
MAX = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    MAX += c
edges.sort()
cnt = 0
for c, a, b in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    cnt += 1
    MAX -= c
    if cnt == N - 1:
        break

if cnt == N-1:
    print(MAX)
else:
    print(-1)