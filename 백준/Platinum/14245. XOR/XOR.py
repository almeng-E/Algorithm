import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = list(map(int, input().split()))

LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

lazy = [0] * SIZE


def range_update(node, s, e, ts, te, v):
    if e < ts or te < s:
        return

    if ts <= s and e <= te:
        lazy[node] ^= v
        return

    if s != e:
        lc = node << 1
        rc = lc + 1
        mid = (s + e) >> 1
        range_update(lc, s, mid, ts, te, v)
        range_update(rc, mid+1, e, ts, te, v)


def point_get(idx):
    tmp = arr[idx]
    idx += LEN
    while idx:
        tmp ^= lazy[idx]
        idx >>= 1
    return tmp


ret = []
M = int(input())
for _ in range(M):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b, c = query[1:]
        range_update(1, 0, LEN-1, a, b, c)

    else:
        a = query[1]
        ret.append(str(point_get(a)))

print('\n'.join(ret))