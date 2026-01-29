import sys
input = sys.stdin.readline

N, M = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

arr = list(map(int, input().split()))

cnt = 0
in_ = [0] * (N+1)
out_ = [0] * (N+1)

# DFS / 오일러 경로 테크닉
stack = []
stack.append((1, 1))    # cur, go_in (1-진입, 0-탈출)
while stack:
    cur, go_in = stack.pop()
    if go_in:
        cnt += 1
        in_[cur] = cnt
        stack.append((cur, 0))
        for nxt in g[cur]:
            if not in_[nxt]:
                stack.append((nxt, 1))
    else:
        out_[cur] = cnt


LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE
lazy = [0] * SIZE

for i in range(1, N+1):
    tree[in_[i] - 1 + LEN] = arr[i-1]

for i in range(LEN-1, 0, -1):
    tree[i] = tree[i*2] ^ tree[i*2 + 1]


def push_down(node, s, e):
    if not lazy[node]:
        return

    if (e - s + 1) & 1:
        tree[node] ^= lazy[node]

    if s != e:
        lazy[node*2] ^= lazy[node]
        lazy[node*2 + 1] ^= lazy[node]
    lazy[node] = 0


def range_update(node, s, e, ts, te, v):
    push_down(node, s, e)
    if e < ts or te < s:
        return
    if ts <= s and e <= te:
        lazy[node] ^= v
        push_down(node, s, e)
        return

    lc = node * 2
    rc = lc + 1
    mid = (s + e) >> 1

    range_update(lc, s, mid, ts, te, v)
    range_update(rc, mid+1, e, ts, te, v)
    tree[node] = tree[lc] ^ tree[rc]


def range_get(node, s, e, ts, te):
    push_down(node, s, e)
    if e < ts or te < s:
        return 0
    if ts <= s and e <= te:
        return tree[node]

    lc = node * 2
    rc = lc + 1
    mid = (s + e) >> 1

    return range_get(lc, s, mid, ts, te) ^ range_get(rc, mid+1, e, ts, te)


ans = []
for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        x = cmd[1]
        l, r = in_[x]-1, out_[x]-1
        ans.append(range_get(1, 0, LEN-1, l, r))
    else:
        x, y = cmd[1:]
        l, r = in_[x]-1, out_[x]-1
        range_update(1, 0, LEN-1, l, r, y)

print('\n'.join(map(str, ans)))

