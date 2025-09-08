import sys
input = sys.stdin.readline


N = int(input())
LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE
arr = list(map(int, input().split()))
for i in range(N):
    tree[i+LEN] = arr[i]
for i in range(LEN-1, 0, -1):
    tree[i] = tree[i*2] + tree[i*2 + 1]

M = int(input())
one_queries = []
two_queries = dict()
t_idx = 0
for q in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        one_queries.append(cmd[1:])

    else:
        k, i, j = cmd[1:]
        if k not in two_queries:
            two_queries[k] = []
        two_queries[k].append((t_idx, i, j))
        t_idx += 1
res = [0] * t_idx

# 오프라인 쿼리
o_idx = 0
for k in sorted(two_queries.keys()):
    while o_idx < k:
        i, v = one_queries[o_idx]
        idx = i + LEN - 1
        tree[idx] = v
        idx >>= 1
        while idx:
            tree[idx] = tree[idx*2] + tree[idx*2 + 1]
            idx >>= 1
        o_idx += 1

    if o_idx == k:
        for t_idx, i, j in two_queries[k]:
            tmp = 0
            l = i + LEN - 1
            r = j + LEN - 1
            while l <= r:
                if l & 1:
                    tmp += tree[l]
                    l += 1
                if not (r & 1):
                    tmp += tree[r]
                    r -= 1
                l >>= 1
                r >>= 1
            res[t_idx] = tmp




for i in res:
    print(i)