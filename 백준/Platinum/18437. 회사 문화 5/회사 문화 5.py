import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())

p = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    graph[p[i]].append(i)


in_ = [0] * (N+1)
out_ = [0] * (N+1)
cnt = 0

stack = []
stack.append((1, 1))    # cur, status(1진입 0진출)
while stack:
    cur, status = stack.pop()
    if status:
        cnt += 1
        in_[cur] = cnt
        stack.append((cur, 0))
        for nxt in graph[cur]:
            stack.append((nxt, 1))
    else:
        out_[cur] = cnt

LEN = 1
while LEN < N:
    LEN <<= 1
tree = [1] * (LEN*2)


def range_set(node, s, e, ts, te, v):
    if te < s or e < ts:
        return
    if ts <= s and e <= te:
        tree[node] = v
        return

    lc = node << 1
    rc = lc + 1
    mid = (s+e) >> 1

    if tree[node] != 2:
        tree[lc] = tree[node]
        tree[rc] = tree[node]

    range_set(lc, s, mid, ts, te, v)
    range_set(rc, mid+1, e, ts, te, v)

    if tree[lc] != tree[rc]:
        tree[node] = 2
    else:
        tree[node] = tree[lc]


def range_get(node, s, e, ts, te):
    global res

    if te < s or e < ts:
        return
    if tree[node] != 2:
        res += tree[node] * (min(e, te) - max(s, ts) + 1)
        return

    lc = node << 1
    rc = lc + 1
    mid = (s+e) >> 1

    range_get(lc, s, mid, ts, te)
    range_get(rc, mid+1, e, ts, te)


out = []
M = int(input())
for _ in range(M):
    cmd, i = map(int, input().split())
    l, r = in_[i], out_[i]-1
    if cmd == 1:
        range_set(1, 0, LEN-1, l, r, 1)
    elif cmd == 2:
        range_set(1, 0, LEN-1, l, r, 0)
    else:
        res = 0
        if l <= r:
            range_get(1, 0, LEN-1, l, r)
        out.append(str(res))

print('\n'.join(out))
