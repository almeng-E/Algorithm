import sys
input = sys.stdin.readline

def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)
    if ref_x == ref_y:
        return
    else:
        p[ref_y] = ref_x
        candy[ref_x] += candy[ref_y]
        kids[ref_x] += kids[ref_y]

N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))
kids = [1] * (N+1)
p = [i for i in range(N+1)]

e_cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    if find_set(a) == find_set(b):
        continue
    else:
        union(a, b)
        e_cnt += 1

    if e_cnt == (N-1):
        break

group_candy = []    # 사탕 , 사람
# 루트 찾기
for i in range(1, N+1):
    if i == p[i]:
        group_candy.append((candy[i], kids[i]))


DP = [0] * K
for candy, kid in group_candy:
    for i in range(K-1, kid-1, -1):
        if DP[i] < DP[i-kid] + candy:
            DP[i] = DP[i-kid] + candy
print(DP[K-1])


