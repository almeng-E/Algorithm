import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, Q1, Q2 = map(int, input().split())
arr = list(map(int, input().split()))

LEN = 1
while LEN < N:
    LEN <<= 1
tree = [0] * (LEN*2)
lazy = [0] * (LEN*2)

for i in range(N):
    tree[i+LEN] = arr[i]
for i in range(LEN-1, 0, -1):
    tree[i] = tree[i*2] + tree[i*2 + 1]


def push_down(node, s, e):
    if lazy[node] == 0:
        return
    tree[node] += (lazy[node] * (e-s+1))

    if s != e:
        lc = node * 2
        rc = lc + 1

        lazy[lc] += lazy[node]
        lazy[rc] += lazy[node]

    lazy[node] = 0


def range_get(node, s, e, ts, te):
    push_down(node, s, e)

    if te < s or e < ts:
        return 0

    if ts <= s and e <= te:
        return tree[node]

    lc = node * 2
    rc = lc + 1
    mid = (s+e) // 2
    return range_get(lc, s, mid, ts, te) + range_get(rc, mid+1, e, ts, te)


def range_update(node, s, e, ts, te, v):
    push_down(node, s, e)

    if te < s or e < ts:
        return

    if ts <= s and e <= te:
        tree[node] += v * (e-s+1)
        if s == e:
            return
        lazy[node*2] += v
        lazy[node*2 + 1] += v
        return

    lc = node * 2
    rc = lc + 1
    mid = (s+e) // 2
    range_update(lc, s, mid, ts, te, v)
    range_update(rc, mid+1, e, ts, te, v)

    tree[node] = tree[lc] + tree[rc]
    return


out = []
for _ in range(Q1+Q2):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        n, m = cmd[1:]
        x = range_get(1, 0, LEN-1, n-1, m-1)
        out.append(str(x))
    else:
        ts, te, l = cmd[1:]
        range_update(1, 0, LEN-1, ts-1, te-1, l)


print('\n'.join(out))