import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline


def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])
    return p[x]

def union_set(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)

    if root_a == root_b:
        return
    else:
        p[root_b] = root_a


V, E = map(int, input().split())

p = [i for i in range(V+1)]
edges = []
visited = [False] * (V+1)

for _ in range(E):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))

# 정렬
edges.sort(key=lambda x: x[2])

cnt = 0
res = 0

for a, b, w in edges:
    if find_parent(a) == find_parent(b):
        continue
    else:
        union_set(a, b)
        cnt += 1
        res += w

    if cnt == V-1:
        break
print(res)