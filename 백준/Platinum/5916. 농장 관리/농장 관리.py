import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs1(cur, bef):
    p[cur] = bef
    depth[cur] = depth[bef] + 1
    cur_max = 0
    for nxt in g[cur]:
        if nxt == bef:
            continue
        size[cur] += dfs1(nxt, cur)
        if cur_max < size[nxt]:
            cur_max = size[nxt]
            heavy_child[cur] = nxt
    return size[cur]


def dfs2(cur, bef):
    global cnt
    in_[cur] = cnt
    cnt += 1
    if heavy_child[cur]:
        nxt = heavy_child[cur]
        head[nxt] = head[cur]
        dfs2(nxt, cur)
    for nxt in g[cur]:
        if nxt != bef and nxt != heavy_child[cur]:
            head[nxt] = nxt
            dfs2(nxt, cur)


def query(u, v, opt):
    global LEN
    ret = 0
    while head[u] != head[v]:
        if depth[head[u]] > depth[head[v]]:
            u, v = v, u
        l = in_[head[v]]
        r = in_[v]
        if opt == 0:
            range_update(1, 0, LEN-1, l, r)
        else:
            ret += range_get(1, 0, LEN-1, l, r)

        v = p[head[v]]

    if depth[u] > depth[v]:
        u, v = v, u
    l = in_[u] + 1      # off-by-one,,,
    r = in_[v]

    if opt == 0:
        range_update(1, 0, LEN-1, l, r)
    else:
        ret += range_get(1, 0, LEN-1, l, r)
        return ret


def push_down(node, s, e):
    if not lazy[node]:
        return
    tree[node] += lazy[node] * (e-s+1)

    if s != e:
        lc = node << 1
        rc = lc | 1
        lazy[lc] += lazy[node]
        lazy[rc] += lazy[node]

    lazy[node] = 0


def range_update(node, s, e, ts, te):
    push_down(node, s, e)
    if e < ts or te < s:
        return
    if ts <= s and e <= te:
        lazy[node] += 1
        push_down(node, s, e)
        return

    mid = (s+e) >> 1
    lc = node << 1
    rc = lc | 1
    range_update(lc, s, mid, ts, te)
    range_update(rc, mid+1, e, ts, te)

    tree[node] = tree[lc] + tree[rc]


def range_get(node, s, e, ts, te):
    push_down(node, s, e)
    if e < ts or te < s:
        return 0
    if ts <= s and e <= te:
        return tree[node]

    mid = (s+e) >> 1
    lc = node << 1
    rc = lc | 1
    return range_get(lc, s, mid, ts, te) + range_get(rc, mid+1, e, ts, te)


N, M = map(int, input().split())
g = [[] for _ in range(N+1)]
p = [0] * (N+1)
size = [1] * (N+1)
depth = [-1] * (N+1)
heavy_child = [0] * (N+1)

in_ = [0] * (N+1)
head = [0] * (N+1)


for _ in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dfs1(1, 0)
cnt = 0
head[1] = 1
dfs2(1, 0)


LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

tree = [0] * SIZE
lazy = [0] * SIZE

ans = []
for _ in range(M):
    cmd = input().split()
    u, v = map(int, cmd[1:])
    if cmd[0] == 'P':
        query(u, v, 0)
    else:
        ans.append(query(u, v, 1))
print('\n'.join(map(str, ans)))

