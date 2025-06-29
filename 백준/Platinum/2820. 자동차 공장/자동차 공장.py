import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
arr = [0] * (N+1)
arr[1] = int(input())

for i in range(2, N+1):
    v, p = map(int, input().split())
    graph[p].append(i)
    arr[i] = v

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
    cmd = input().split()
    if cmd[0] == 'p':
        a = int(cmd[1])
        x = int(cmd[2])
        range_update(1, 0, LEN-1, in_o[a], out_o[a] - 1, x)

    elif cmd[0] == 'u':
        a = int(cmd[1])
        print(arr[a] + point_get(1, 0, LEN-1, in_o[a] - 1))
