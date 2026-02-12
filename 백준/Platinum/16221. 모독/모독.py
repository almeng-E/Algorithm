import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)



def defile(node, s, e):
    if is_alive[node]:
        return tree[node]

    if s == e:
        return 0

    lc = node << 1
    rc = lc + 1
    mid = (s+e) >> 1
    if is_alive[lc]:
        return tree[lc] + defile(rc, mid+1, e)
    else:
        return defile(lc, s, mid)


def check_alive(idx):
    while idx:
        if is_alive[idx * 2] and is_alive[idx * 2 + 1]:
            is_alive[idx] = 1
        else:
            is_alive[idx] = 0
        idx >>= 1

Q = int(input())
LEN = 1
while LEN < 1_000_000:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE
is_alive = [0] * SIZE

ans = []

for _ in range(Q):
    T, K = map(int, input().split())
    if T == 1:
        idx = K-1+LEN
        while idx:
            tree[idx] += 1
            idx >>= 1

        idx = K-1+LEN
        if not is_alive[idx]:
            is_alive[idx] = 1
            idx >>= 1
            check_alive(idx)

    else:
        idx = K-1+LEN
        while idx:
            tree[idx] -= 1
            idx >>= 1
        idx = K-1+LEN
        if tree[idx] == 0:
            is_alive[idx] = 0
            idx >>= 1
            check_alive(idx)

    ans.append(defile(1, 0, LEN-1))
print('\n'.join(map(str, ans)))
