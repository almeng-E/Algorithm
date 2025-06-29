import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N, M = map(int, input().split())
p = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for i in range(2, N+1):
    graph[p[i]].append(i)

in_o = [0] * (N+1)
out_o = [0] * (N+1)
cnt = 0

stack = []
stack.append((1, 1))
while stack:
    cur, status = stack.pop()
    if status:
        cnt += 1
        in_o[cur] = cnt
        stack.append((cur, 0))
        for nxt in graph[cur]:
            stack.append((nxt, 1))
    else:
        out_o[cur] = cnt

# lazy seg...?? 그냥 segtree;
LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

lazy = [0] * SIZE


def range_update(node, s, e, ts, te, val):
    if te < s or e < ts:
        return
    if ts <= s and e <= te:
        lazy[node] += val
        return

    lc = node << 1
    rc = lc + 1
    mid = (s + e) >> 1

    range_update(lc, s, mid, ts, te, val)
    range_update(rc, mid+1, e, ts, te, val)


def point_get(node, s, e, tg):
    if s == e:
        return lazy[node]
    mid = (s + e) >> 1
    if tg <= mid:
        return lazy[node] + point_get(node << 1, s, mid, tg)
    else:
        return lazy[node] + point_get((node << 1)+1, mid+1, e, tg)


for _ in range(M):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        i, w = cmd[1], cmd[2]
        range_update(1, 0, LEN-1, in_o[i] - 1, out_o[i] - 1, w)

    elif cmd[0] == 2:
        i = cmd[1]
        print(point_get(1, 0, LEN-1, in_o[i] - 1))