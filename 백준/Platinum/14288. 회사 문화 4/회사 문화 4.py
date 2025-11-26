import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

p = [0] + list(map(int, input().split()))
for i in range(2, n + 1):
    graph[p[i]].append(i)
offset = [0] * (n+1)

# 오일러 경로... 트리 펼치기
cnt = 0
in_o = [0] * (n + 1)
out_o = [0] * (n + 1)

# DFS
stack = []
stack.append((1, 1))  # cur, status(1-진입 0-탈출)
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

# lazy-seg-tree
LEN = 1
while LEN < n:
    LEN <<= 1
SIZE = LEN << 1

seg_tree = [0] * SIZE
lazy = [0] * SIZE

down = 1

def push_down(node, s, e):
    if not lazy[node]:
        return

    seg_tree[node] += lazy[node]

    if s != e:
        lazy[node << 1] += lazy[node]
        lazy[(node << 1) + 1] += lazy[node]

    lazy[node] = 0


def range_update(node, s, e, ts, te, val):
    push_down(node, s, e)

    if te < s or e < ts:
        return

    lc = node << 1
    rc = lc + 1

    if ts <= s and e <= te:
        seg_tree[node] += val
        if s == e:
            return

        lazy[lc] += val
        lazy[rc] += val
        return

    mid = (s + e) >> 1
    range_update(lc, s, mid, ts, te, val)
    range_update(rc, mid + 1, e, ts, te, val)

    seg_tree[node] = seg_tree[lc] + seg_tree[rc]


def point_get(node, s, e, target):
    push_down(node, s, e)

    if s == e:
        return

    mid = (s + e) >> 1
    lc = node << 1
    rc = lc + 1
    if s <= target <= mid:
        point_get(lc, s, mid, target)
    else:
        point_get(rc, mid + 1, e, target)


for _ in range(m):
    cmd = list(map(int, input().split()))

    # range-update
    if cmd[0] == 1:
        node = cmd[1]
        w = cmd[2]
        if down:
            left = in_o[node] - 1
            right = out_o[node] - 1
            range_update(1, 0, LEN - 1, left, right, w)
        else:
            while node > 0:
                offset[node] += w
                node = p[node]


    elif cmd[0] == 2:
        node = cmd[1]
        idx = in_o[node] - 1
        point_get(1, 0, LEN - 1, idx)
        print(offset[node] + seg_tree[idx + LEN])

    elif cmd[0] == 3:
        down ^= 1
