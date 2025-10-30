import sys
input = sys.stdin.readline
from itertools import combinations
import math



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
edges = []
pos = []
p = [i for i in range(N)]
e_cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    pos.append((a, b))

for _ in range(M):
    a, b = map(int, input().split())
    if find(a-1) != find(b-1):
        e_cnt += 1
        union(a-1, b-1)


nCr = combinations(range(N), 2)
for comb in nCr:
    a, b = comb
    if find(a) == find(b):
        continue
    edges.append((a, b, math.sqrt((pos[a][0] - pos[b][0]) ** 2 + (pos[a][1] - pos[b][1]) ** 2)))

edges.sort(key=lambda x: x[2])

res = 0
for a, b, c in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    res += c
    e_cnt += 1

    if e_cnt == (N-1):
        break
print(f'{round(res, 2):.2f}')