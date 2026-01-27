import sys
input = sys.stdin.readline



N = int(input())
arr = list(map(int, input().split()))

LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE
cnt = [0] * SIZE


def push_down(node, s, e):
    if not tree[node] and not cnt[node]:
        return

    if s != e:
        lc = node << 1
        rc = lc + 1
        tree[lc] += tree[node]
        cnt[lc] += cnt[node]
        mid = (s + e) >> 1
        tree[rc] += tree[node] + (mid - s + 1) * cnt[node]
        cnt[rc] += cnt[node]

        tree[node] = 0
        cnt[node] = 0


def range_update(node, s, e, ts, te):
    if e < ts or te < s:
        return

    if ts <= s and e <= te:
        cnt[node] += 1
        tree[node] += (s - ts + 1)
        return

    lc = node << 1
    rc = lc + 1
    mid = (s + e) >> 1
    range_update(lc, s, mid, ts, te)
    range_update(rc, mid+1, e, ts, te)


def point_get(node, s, e, tg):
    push_down(node, s, e)

    if tg < s or e < tg:
        return
    if s == e == tg:
        return

    mid = (s+e) >> 1
    if tg <= mid:
        point_get(node << 1, s, mid, tg)
    else:
        point_get((node << 1) + 1, mid+1, e, tg)

ans = []
Q = int(input())
for _ in range(Q):
    cmd = map(int, input().split())
    if next(cmd) == 1:
        L, R = next(cmd), next(cmd)
        range_update(1, 0, LEN-1, L-1, R-1)
    else:
        X = next(cmd)
        point_get(1, 0, LEN-1, X-1)
        ans.append(arr[X-1] + tree[X-1 + LEN])
print('\n'.join(map(str, ans)))