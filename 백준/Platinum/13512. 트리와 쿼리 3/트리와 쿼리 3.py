import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)



def dfs1(cur, bef):
    dep[cur] = dep[bef] + 1
    p[cur] = bef
    max_size = 0
    for nxt in g[cur]:
        if nxt == bef:
            continue
        sz[cur] += dfs1(nxt, cur)
        if max_size < sz[nxt]:
            max_size = sz[nxt]
            heavy_child[cur] = nxt
    return sz[cur]


def dfs2(cur, bef):
    global cnt
    cnt += 1
    in_[cur] = cnt
    ori_[cnt] = cur

    if heavy_child[cur]:
        nxt = heavy_child[cur]
        top[nxt] = top[top[cur]]
        dfs2(nxt, cur)

    for nxt in g[cur]:
        if nxt != bef and nxt != heavy_child[cur]:
            top[nxt] = nxt
            dfs2(nxt, cur)


def point_update(idx):
    tree[idx] ^= 1
    idx >>= 1
    while idx:
        tree[idx] = tree[idx<<1] + tree[idx<<1 | 1]
        idx >>= 1


def range_get(node, s, e, ts, te):
    if not tree[node]:
        return -1

    if e < ts or te < s:
        return -1

    if s == e:
        if tree[node]:
            return node
        else:
            return -1

    lc = node << 1
    rc = lc + 1
    mid = (s + e) >> 1

    ret = range_get(lc, s, mid, ts, te)
    if ret != -1:
        return ret

    ret = range_get(rc, mid+1, e, ts, te)
    return ret


def query(node):
    path = []
    while top[node] != 1:
        path.append((top[node], node))
        node = p[top[node]]
    path.append((1, node))

    for a, b in reversed(path):
        ret = range_get(1, 0, LEN-1, in_[a], in_[b])
        if ret != -1:
            return ret
    return -1

N = int(input())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

p = [0] * (N+1)
dep = [-1] * (N+1)
sz = [1] * (N+1)
heavy_child = [0] * (N+1)
dfs1(1, 0)

top = [0] * (N+1)
in_ = [0] * (N+1)
ori_ = [0] * (N+1)
cnt = -1
top[1] = 1
dfs2(1, 0)

LEN = 1
while LEN < N:
    LEN <<= 1
tree = [0] * (LEN << 1)
ans = []
M = int(input())
for _ in range(M):
    cmd, v = map(int, input().split())
    if cmd == 1:
        point_update(in_[v] + LEN)
    else:
        ret = query(v)
        if ret != -1:
            ret = ori_[ret-LEN]
        ans.append(ret)

print('\n'.join(map(str, ans)))

