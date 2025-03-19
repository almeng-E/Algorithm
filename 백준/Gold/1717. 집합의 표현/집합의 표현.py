import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union_set(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return
    else:
        p[root_x] = root_y



N, M = map(int, input().split())

p = [i for i in range(N+1)]

for _ in range(M):
    c, a, b = map(int, input().split())

    if c == 0:
        union_set(a, b)
    else:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')