import sys
input = sys.stdin.readline

N = int(input())
graph = [set() for _ in range(N)]
for i in range(N):
    r = input()
    for j in range(N):
        if r[j] == 'Y':
            graph[i].add(j)

res = 0
for i in range(N):
    f = graph[i].copy()
    for mf in graph[i]:
        f = f.union(graph[mf])
    if i in f:
        f.remove(i)
    res = max(res, len(f))
print(res)