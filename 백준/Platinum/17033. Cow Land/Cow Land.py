import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def dfs1(cur, bef):
    p[cur] = bef
    dep[cur] = dep[bef] + 1
    m_s = 0
    for nxt in g[cur]:
        if nxt == bef:
            continue
        sz[cur] += dfs1(nxt, cur)
        if m_s < sz[nxt]:
            m_s = sz[nxt]
            h_ch[cur] = nxt
    return sz[cur]


def dfs2(cur, bef):
    global cnt
    in_[cur] = cnt
    cnt += 1
    if h_ch[cur]:
        nxt = h_ch[cur]
        head[nxt] = head[cur]
        dfs2(nxt, cur)
    for nxt in g[cur]:
        if nxt != bef and nxt != h_ch[cur]:
            head[nxt] = nxt
            dfs2(nxt, cur)


def query(u, v):
    ret = 0
    while head[u] != head[v]:
        if dep[head[u]] > dep[head[v]]:
            u, v = v, u
        l = in_[head[v]] + LEN
        r = in_[v] + LEN
        while l <= r:
            if l & 1:
                ret ^= tree[l]
                l += 1
            if not (r & 1):
                ret ^= tree[r]
                r -= 1
            l >>= 1
            r >>= 1

        v = p[head[v]]
    if dep[u] > dep[v]:
        u, v = v, u
    l = in_[u] + LEN
    r = in_[v] + LEN
    while l <= r:
        if l & 1:
            ret ^= tree[l]
            l += 1
        if not (r & 1):
            ret ^= tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    return ret


N, Q = map(int, input().split())
g = [[] for _ in range(N+1)]

p = [0] * (N+1)
dep = [0] * (N+1)
sz = [1] * (N+1)
h_ch = [0] * (N+1)

head = [0] * (N+1)
in_ = [0] * (N+1)

e = [0] + list(map(int, input().split()))

for _ in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


dfs1(1, 0)

head[1] = 1
cnt = 0
dfs2(1, 0)


LEN = 1
while LEN < N:
    LEN <<= 1

tree = [0] * (LEN << 1)

for i in range(1, N+1):
    tree[in_[i]+LEN] = e[i]
for i in range(LEN-1, 0, -1):
    tree[i] = tree[i<<1] ^ tree[i<<1 | 1]

ans = []
for _ in range(Q):
    cmd, i, j = map(int, input().split())
    if cmd == 1:
        idx = in_[i] + LEN
        tree[idx] = j
        idx >>= 1
        while idx:
            tree[idx] = tree[idx<<1] ^ tree[idx<<1 | 1]
            idx >>= 1
    else:
        ans.append(query(i, j))

print('\n'.join(map(str, ans)))
