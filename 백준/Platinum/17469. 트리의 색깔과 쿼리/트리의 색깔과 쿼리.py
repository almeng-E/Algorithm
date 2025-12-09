import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
tg = [i for i in range(N+1)]
for i in range(2, N+1):
    tg[i] = int(input())
p = [i for i in range(N+1)]

c = [set() for _ in range(N+1)]
for i in range(1, N+1):
    c[i].add(int(input()))

queries = []
for _ in range(N+Q-1):
    queries.append(list(map(int, input().split())))


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def unionS(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        if len(c[ra]) < len(c[rb]):
            p[ra] = rb
            c[rb].update(c[ra])
        else:
            p[rb] = ra
            c[ra].update(c[rb])


out = []
for x, a in reversed(queries):
    if x == 1:
        unionS(a, tg[a])
    else:
        out.append(len(c[find(a)]))

print('\n'.join(map(str, out[::-1])))
