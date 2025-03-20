
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
        # 어디로 병합할까 ?
        if cost[root_a] > cost[root_b]:
            p[root_a] = root_b
        else:
            p[root_b] = root_a


N, M, k = map(int, input().split())

cost = [0] + list(map(int, input().split()))

p = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    if find_parent(a) == find_parent(b):
        continue
    else:
        union_set(a, b)


total_cost = 0
for i in range(1, N+1):
    if p[i] == i:
        total_cost += cost[i]

if total_cost > k:
    print('Oh no')
else:
    print(total_cost)
