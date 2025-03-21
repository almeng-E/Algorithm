import sys
input = sys.stdin.readline
def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])
    return p[x]


def union_set(a, b):
    rf_a = find_parent(a)
    rf_b = find_parent(b)
    if rf_a != rf_b:
        p[rf_b] = rf_a


N, M = map(int, input().split())
p = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    union_set(a, b)

cl = list(map(int, input().split()))
res = 0
for i in range(len(cl)-1):
    if find_parent(cl[i]) != find_parent(cl[i+1]):
        res += 1

print(res)