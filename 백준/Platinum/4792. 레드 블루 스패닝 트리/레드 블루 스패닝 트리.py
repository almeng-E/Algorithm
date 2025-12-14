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


def make_tree(edges):
    global cnt
    for u, v in edges:
        if find(u) != find(v):
            union(u, v)
            cnt += 1
        if cnt == n-1:
            break


while True:
    n, m, k = map(int, input().split())
    if n == 0:
        break

    blues = []
    reds = []
    for _ in range(m):
        c, f, t = input().split()
        if c == 'B':
            blues.append((int(f), int(t)))
        else:
            reds.append((int(f), int(t)))

    p = [i for i in range(n+1)]
    MIN = 0
    cnt = 0
    make_tree(reds)
    MIN = n-1-cnt

    cnt = 0
    p = [i for i in range(n+1)]
    make_tree(blues)
    MAX = cnt

    if MIN <= k <= MAX:
        print(1)
    else:
        print(0)