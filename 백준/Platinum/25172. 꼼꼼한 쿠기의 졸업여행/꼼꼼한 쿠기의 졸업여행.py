import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        p[ra] = rb


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queries = []
for _ in range(N):
    queries.append(int(input()))

alive = [False] * (N+1)
p = [i for i in range(N+1)]
res = []
roots = 0

for x in reversed(queries):
    if roots == 1:
        res.append(1)
    else:
        res.append(0)
    alive[x] = True
    roots += 1
    for y in graph[x]:
        if alive[y] and (find(x) != find(y)):
            roots -= 1
            union(x, y)
if roots == 1:
    res.append(1)
else:
    res.append(0)

for i in reversed(res):
    if i:
        print('CONNECT')
    else:
        print('DISCONNECT')

