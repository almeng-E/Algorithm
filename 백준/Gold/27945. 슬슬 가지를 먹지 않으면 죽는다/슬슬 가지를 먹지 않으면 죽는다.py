import sys
input = sys.stdin.readline


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    rt_a = find(a)
    rt_b = find(b)
    if rt_a == rt_b:
        return 0
    else:
        p[rt_a] = rt_b
        return 1


N, M = map(int, input().split())
p = [i for i in range(N+1)]
edges = [tuple(map(int, input().split())) for _ in range(M)]

edges.sort(key=lambda x: x[2])
CUR_DAY = 1
CNT = 0
for a, b, t in edges:
    if union(a, b):
        CNT += 1
        if CUR_DAY == t:
            CUR_DAY += 1
        else:
            break
    if CNT == N-1:
        break
print(CUR_DAY)