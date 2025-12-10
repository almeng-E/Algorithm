import sys
input = sys.stdin.readline
sys.setrecursionlimit(400_000)
N = int(input())
g = [0] + list(map(int, input().split()))

M = int(input())
queries = []
connected = [True] * (N+1)
for _ in range(M):
    cmd, x = map(int, input().split())
    queries.append([cmd, x])
    if cmd == 2:
        connected[x] = False


p = [i for i in range(N+1)]


def find(x):
    if p[x] == x:
        return p[x]
    if p[x] == 0:
        return 0
    p[x] = find(p[x])
    return p[x]


def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        p[ra] = rb
    else:
        p[ra] = 0
        p[rb] = 0


for i in range(N+1):
    if connected[i] and g[i] != 0:
        union(i, g[i])

ret = []
for cmd, x in reversed(queries):
    if cmd == 1:
        ret.append(find(x))
    else:

        union(x, g[x])

for r in reversed(ret):
    if r == 0:
        print('CIKLUS')
    else:
        print(r)