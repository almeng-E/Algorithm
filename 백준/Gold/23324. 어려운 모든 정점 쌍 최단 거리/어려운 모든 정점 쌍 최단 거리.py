import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(a, b):
    rt_a = find(a)
    rt_b = find(b)
    if rt_a == rt_b:
        return 0

    if (rt_a, rt_b) == (L, R) or (rt_a, rt_b) == (R, L):
        return 2
    if rt_a == L or rt_a == R:
        sz[rt_a] += sz[rt_b]
        p[rt_b] = rt_a
    elif rt_b == L or rt_b == R:
        sz[rt_b] += sz[rt_a]
        p[rt_a] = rt_b
    else:
        sz[rt_b] += sz[rt_a]
        p[rt_a] = rt_b

    return 1


N, M, K = map(int, input().split())
edges = []
for i in range(1, M+1):
    a, b = map(int, input().split())
    if i != K:
        edges.append((a, b))
    else:
        L, R = a, b

p = [i for i in range(N+1)]
sz = [1 for _ in range(N+1)]

# cnt = 0
for a, b in edges:
    ret = union(a, b)
    if ret == 2:
        sz[L], sz[R] = 0, 0
        break
    # cnt += ret
    # if cnt == N-2:
    #     break
print(sz[L]*sz[R])