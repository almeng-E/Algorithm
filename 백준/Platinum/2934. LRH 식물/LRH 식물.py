import sys
input = sys.stdin.readline

N = int(input())

LEN = 1 << 17
SIZE = LEN << 1

tree = [0] * SIZE
lazy = [0] * SIZE


def push_down(node, s, e):
    if not lazy[node]: return
    tree[node] += lazy[node]

    if s != e:
        lc = node << 1
        rc = lc + 1
        lazy[lc] += lazy[node]
        lazy[rc] += lazy[node]
    lazy[node] = 0


def range_update(node, s, e, ts, te):
    push_down(node, s, e)
    if e < ts or te < s:
        return

    if ts <= s and e <= te:
        lazy[node] += 1
        push_down(node, s, e)
        return

    lc = node << 1
    rc = lc + 1
    mid = (s+e) >> 1
    range_update(lc, s, mid, ts, te)
    range_update(rc, mid+1, e, ts, te)

    tree[node] = tree[lc] + tree[rc]


def point_update(node, s, e, tg):
    global cnt
    push_down(node, s, e)
    if e < tg or tg < s:
        return
    if s == e == tg:
        cnt += tree[node] - 1
        tree[node] = 0
        return

    lc = node << 1
    rc = lc + 1
    mid = (s+e) >> 1
    if tg <= mid:
        point_update(lc, s, mid, tg)
    else:
        point_update(rc, mid+1, e, tg)
    tree[node] = tree[lc] + tree[rc]


ans = []
for _ in range(N):
    L, R = map(int, input().split())
    range_update(1, 0, LEN-1, L, R)
    cnt = 0
    point_update(1, 0, LEN - 1, L)
    point_update(1, 0, LEN - 1, R)
    ans.append(str(cnt))
print('\n'.join(ans))

