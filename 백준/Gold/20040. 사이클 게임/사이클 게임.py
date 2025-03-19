import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def make_set(n):
    p = [i for i in range(N)]
    return p


def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])
    return p[x]


def union_parent(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)

    if root_a == root_b:
        return
    else:
        p[root_a] = root_b


N, M = map(int, input().split())

graph = [[] for _ in range(N)]
p = make_set(N)

for cnt in range(1, M+1):
    a, b = map(int, input().split())
    if find_parent(a) != find_parent(b):
        union_parent(a, b)

    else:
        print(cnt)
        break

else:
    print(0)