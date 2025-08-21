import sys
input = sys.stdin.readline

LEN = 1 << 20

tree = [0] * (LEN << 1)


def get(node, s, e, cnt):
    global res, LEN
    if s == e:
        res = node - LEN + 1
        return

    lc = node << 1
    rc = lc + 1
    mid = (s + e) // 2
    if tree[lc] < cnt:
        get(rc, mid+1, e, cnt - tree[lc])
    else:
        get(lc, s, mid, cnt)


def point_update(idx, v):
    global tree

    tree[idx] += v
    idx >>= 1
    while idx >= 1:
        tree[idx] += v
        idx >>= 1


N = int(input())
for _ in range(N):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        B = cmd[1]
        res = 0
        get(1, 0, LEN-1, B)
        print(res)

        point_update(res + LEN - 1, -1)

    else:
        B = cmd[1]
        C = cmd[2]

        point_update(B+LEN-1, C)
