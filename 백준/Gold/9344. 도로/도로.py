import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    rta = find(a)
    rtb = find(b)
    if rta != rtb:
        p[rtb] = rta


T = int(input())
for _ in range(T):
    N, M, x, y = map(int, input().split())
    edges = []
    p = [i for i in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        if u > v:
            u, v = v, u
        edges.append((u, v, w))

    if x > y:
        x, y = y, x
    edges.sort(key=lambda x: x[2])
    cnt = 0
    ret = 'NO'
    for a, b, w in edges:
        if find(a) != find(b):
            union(a, b)
            cnt += 1
            if (a, b) == (x, y):
                ret = 'YES'
        if cnt == N-1:
            break
    print(ret)