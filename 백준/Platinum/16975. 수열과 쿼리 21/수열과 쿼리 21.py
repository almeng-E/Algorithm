import sys
input = sys.stdin.readline


N = int(input())
LEN = 1
while LEN <= N:
    LEN <<= 1
SIZE = LEN << 1

lazy = [0] * SIZE

arr = [0] + list(map(int, input().split()))


def lazy_update(node, s, e, ts, te, val):
    # 범위 밖
    if e < ts or te < s:
        return

    # 완전 포함
    if ts <= s and e <= te:
        lazy[node] += val
        return

    # 더 들어가야 함
    mid = (s + e) // 2
    lazy_update((node << 1), s, mid, ts, te, val)
    lazy_update((node << 1) + 1, mid + 1, e, ts, te, val)



def get_point(node, s, e, idx):
    if s == e:
        return arr[idx] + lazy[node]

    mid = (s + e) >> 1
    lc = node << 1
    rc = lc + 1

    lazy[lc] += lazy[node]
    lazy[rc] += lazy[node]
    lazy[node] = 0

    if idx <= mid:
        return get_point(lc, s, mid, idx)
    else:
        return get_point(rc, mid + 1, e, idx)


M = int(input())
for _ in range(M):
    cmd = list(map(int, input().split()))

    # update
    if cmd[0] == 1:
        _, i, j, val = cmd
        lazy_update(1, 1, LEN, i, j, val)

    # get
    if cmd[0] == 2:
        _, x = cmd
        print(get_point(1, 1, LEN, x))