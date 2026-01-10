import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input())
arr = list(map(int, input().split()))

# 트리, lazy트리 구성
LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE
lazy = [0] * SIZE

for i in range(N):
    tree[LEN+i] = arr[i]
for i in range(LEN-1, 0, -1):
    tree[i] = tree[i*2] ^ tree[i*2 + 1]


def push_down(node, s, e):
    if not lazy[node]:
        return
    # 최신화
    if (e-s+1) & 1:
        tree[node] ^= lazy[node]
    # 전파
    if s != e:
        lc = node << 1
        rc = lc + 1
        lazy[lc] ^= lazy[node]
        lazy[rc] ^= lazy[node]
    # 초기화
    lazy[node] = 0


def range_update(node, s, e, ts, te, v):
    push_down(node, s, e)

    # 범위 out
    if te < s or e < ts:
        pass
    # 완전 포함
    elif ts <= s and e <= te:
        lazy[node] = v
        push_down(node, s, e)
    # 더 들어가야함
    else:
        lc = node << 1
        rc = lc + 1
        mid = (s+e) >> 1
        range_update(lc, s, mid, ts, te, v)
        range_update(rc, mid+1, e, ts, te, v)

        tree[node] = tree[lc] ^ tree[rc]

def range_get(node, s, e, ts, te):
    global res
    push_down(node, s, e)

    if te < s or e < ts:
        return
    elif ts <= s and e <= te:
        res ^= tree[node]
    else:
        lc = node << 1
        rc = lc + 1
        mid = (s+e) >> 1
        range_get(lc, s, mid, ts, te)
        range_get(rc, mid+1, e, ts, te)


out = []
M = int(input())
for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        i, j, k = cmd[1:]
        range_update(1, 0, LEN-1, i, j, k)
    else:
        i, j = cmd[1:]
        res = 0
        range_get(1, 0, LEN - 1, i, j)
        out.append(str(res))

print('\n'.join(out))


