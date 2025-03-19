# disjoint-set ...

def make_set(n):
    p = [i for i in range(n+1)]
    return p

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return
    else:
        p[root_x] = root_y


T = int(input())
for TC in range(T):
    N, M = map(int, input().split())

    p = make_set(N)
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
    res = 0
    for i in range(1, N+1):
        if i == p[i]:
            res += 1
    print(f'#{TC+1} {res}')