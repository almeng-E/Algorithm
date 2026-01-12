import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE
lazy = [0] * SIZE


def push_down(node, s, e):
    if not lazy[node]:
        return
    else:
        tree[node] = (e-s+1) - tree[node]

    if s != e:
        lc = node << 1
        rc = lc + 1
        lazy[lc] ^= 1
        lazy[rc] ^= 1

    lazy[node] = 0


def range_update(node, s, e, ts, te):
    push_down(node, s, e)

    if e < ts or te < s:
        return
    if ts <= s and e <= te:
        lazy[node] ^= 1
        push_down(node, s, e)
        return

    lc = node << 1
    rc = lc + 1
    mid = (s+e) >> 1
    range_update(lc, s, mid, ts, te)
    range_update(rc, mid+1, e, ts, te)

    tree[node] = tree[lc] + tree[rc]


def range_get(node, s, e, ts, te):
    global ret
    push_down(node, s, e)
    if e < ts or te < s:
        return
    if ts <= s and e <= te:
        ret += tree[node]
        return
    lc = node << 1
    rc = lc + 1
    mid = (s+e) >> 1
    range_get(lc, s, mid, ts, te)
    range_get(rc, mid+1, e, ts, te)


res = []
for _ in range(M):
    q, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if q == 0:
        range_update(1, 0, LEN-1, a, b)
    else:
        ret = 0
        range_get(1, 0, LEN-1, a, b)
        res.append(str(ret))
print('\n'.join(res))