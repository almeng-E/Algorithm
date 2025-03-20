import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

# 크루스칼
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

N = int(input())
M = int(input())

p = [i for i in range(N+1)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

cnt = 0
res = 0

for a, b, c in edges:
    if find_parent(a) != find_parent(b):
        union_set(a, b)
        cnt += 1
        res += c

    if cnt == N-1:
        break
print(res)


