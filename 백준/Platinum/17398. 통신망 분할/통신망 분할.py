import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())

edges = [[]]
for _ in range(M):
    edges.append(list(map(int, input().split())))

can_use = [True] * (M+1)

# 오프라인 쿼리 저장
QUERIES = []
for _ in range(Q):
    a = int(input())
    QUERIES.append(a)
    can_use[a] = False

# 크루스칼
p = [i for i in range(N+1)]
size = [1] * (N+1)


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
        size[root_a] += size[root_b]

# 초기 mst 구성
for i in range(1, M+1):
    if can_use[i]:
        x, y = edges[i]
        union_set(x, y)


# 쿼리 역순 수행
res = 0
for q in reversed(QUERIES):
    x, y = edges[q]
    if find_parent(x) == find_parent(y):
        continue
    else:
        res += size[find_parent(x)] * size[find_parent(y)]
        union_set(x, y)

print(res)