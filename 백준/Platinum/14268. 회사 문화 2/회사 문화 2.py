import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

p = [0] + list(map(int, input().split()))
for i in range(2, n+1):
    graph[p[i]].append(i)


LEN = 1
while LEN < n:
    LEN <<= 1
SIZE = LEN << 1

seg_tree = [0] * SIZE
lazy = [0] * SIZE

cnt = 0
in_o = [0] * (n+1)
out_o = [0] * (n+1)



stack = []
stack.append((1, 1))    # cur, status(1-진입 0-탈출)
while stack:
    cur, go_in = stack.pop()
    if go_in:
        cnt += 1
        in_o[cur] = cnt
        stack.append((cur, 0))
        for nxt in graph[cur]:
            stack.append((nxt, 1))
    else:
        out_o[cur] = cnt

        
def range_update(node, s, e, ts, te, val):
    if e < ts or te < s:
        return

    if ts <= s and e <= te:
        lazy[node] += val
        return

    mid = (s + e) >> 1
    lc = node << 1
    rc = lc + 1
    range_update(lc, s, mid, ts, te, val)
    range_update(rc, mid+1, e, ts, te, val)


def point_get(node, s, e, target):
    if s == e:
        return seg_tree[node] + lazy[node]

    mid = (s + e) >> 1
    lc = node << 1
    rc = lc + 1

    lazy[lc] += lazy[node]
    lazy[rc] += lazy[node]
    lazy[node] = 0

    if target <= mid:
        return point_get(lc, s, mid, target)
    else:
        return point_get(rc, mid+1, e, target)


for _ in range(m):
    cmd = list(map(int, input().split()))

    # range-update
    if cmd[0] == 1:
        node = cmd[1]
        w = cmd[2]
        left = in_o[node] - 1
        right = out_o[node] - 1
        range_update(1, 0, LEN-1, left, right, w)

    elif cmd[0] == 2:
        node = cmd[1]
        print(point_get(1, 0, LEN-1, in_o[node] - 1))



