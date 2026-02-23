import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)


def can_group(a, b):
    ax, ay, ar = coords[a]
    bx, by, br = coords[b]
    if (ar+br) ** 2 >= (ax-bx) ** 2 + (ay-by) ** 2:
        return True
    else:
        return False


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    rt_a = find(a)
    rt_b = find(b)
    if rt_a != rt_b:
        p[rt_b] = rt_a


T = int(input())
for _ in range(T):
    N = int(input())
    coords = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]

    for i in range(N):
        for j in range(i, N):
            if find(i) != find(j) and can_group(i, j):
                union(i, j)

    print(len(set(find(i) for i in range(N))))
