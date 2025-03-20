import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)


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

while True:
    N, M = map(int, input().split())
    if N == 0: break

    p = [i for i in range(N+1)]
    edges = []
    before = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        before += c
    edges.sort(key=lambda x: x[2])

    e_cnt = 0

    for a, b, c in edges:
        if find_parent(a) == find_parent(b):
            continue
        else:
            union_set(a, b)
            e_cnt += 1
            before -= c
        if e_cnt == (N-1):
            break

    print(before)