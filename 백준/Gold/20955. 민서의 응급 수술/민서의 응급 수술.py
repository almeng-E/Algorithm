import sys
input = sys.stdin.readline

def 부모찾아잉(x):
    if p[x] != x:
        p[x] = 부모찾아잉(p[x])
    return p[x]

def 합치라잉(a, b):
    ref_a = 부모찾아잉(a)
    ref_b = 부모찾아잉(b)
    if ref_a == ref_b:
        return

    if ranks[ref_a] < ranks[ref_b]:
        p[ref_a] = ref_b
    elif ranks[ref_a] > ranks[ref_b]:
        p[ref_b] = ref_a
    else:
        p[ref_a] = ref_b
        ranks[ref_b] += 1


N, M = map(int, input().split())

p = [i for i in range(N+1)]
ranks = [0] * (N+1)

res = -1
for _ in range(M):
    a, b = map(int, input().split())
    if 부모찾아잉(a) == 부모찾아잉(b):
        res += 1
    else:
        합치라잉(a, b)

for i in range(1, N+1):
    if i == p[i]:
        res += 1
print(res)