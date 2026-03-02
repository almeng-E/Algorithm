import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs1(cur):
    max_size = 0
    for nxt in g[cur]:
        depth[nxt] = depth[cur] + 1
        size[cur] += dfs1(nxt)
        if max_size < size[nxt]:
            max_size = size[nxt]
            heavy_child[cur] = nxt
    return size[cur]


def dfs2(cur):
    global cnt
    in_[cur] = cnt
    in_rev[cnt] = cur
    cnt += 1
    if heavy_child[cur]:
        nxt = heavy_child[cur]
        head[nxt] = head[cur]
        dfs2(nxt)
    for nxt in g[cur]:
        if nxt == heavy_child[cur]:
            continue
        head[nxt] = nxt
        dfs2(nxt)


def range_get(l, r):
    ret = 0
    while l <= r:
        if l & 1:
            ret = max(ret, tree[l])
            l += 1
        if not (r & 1):
            ret = max(ret, tree[r])
            r -= 1
        l >>= 1
        r >>= 1
    return ret


def get_root(x):
    while p[x] != x:
        l = in_[head[x]] + LEN
        r = in_[x] + LEN
        x = p[in_rev[range_get(l, r)]]
    return x


def check(u, v):
    if get_root(u) != get_root(v):
        return 0
    return 1


def cut(x):
    p[x] = x
    idx = in_[x] + LEN
    tree[idx] = in_[x]
    idx >>= 1
    while idx:
        tree[idx] = max(tree[idx<<1], tree[idx<<1 | 1])
        idx >>= 1


N, Q = map(int, input().split())
g = [[] for _ in range(N+1)]
p = [1] * (N+1)
size = [1] * (N+1)
depth = [-1] * (N+1)
heavy_child = [0] * (N+1)

in_rev = [0] * (N+1)
in_ = [0] * (N+1)
head = [0] * (N+1)

for i in range(1, N):
    a = int(input())
    p[i+1] = a
    g[a].append(i+1)


depth[1] = 0
dfs1(1)
head[1] = 1
cnt = 0
dfs2(1)

LEN = 1
while LEN < N:
    LEN <<= 1
tree = [0] * (LEN << 1)

for i in range(1, N+1):
    tree[in_[i]+LEN] = in_[head[i]]
for i in range(LEN-1, 0, -1):
    tree[i] = max(tree[i<<1], tree[i<<1 | 1])


out = ['NO', 'YES']
ans = []
for _ in range(Q):
    b, c, d = map(int, input().split())
    ret = check(b, c)
    ans.append(out[ret])
    if d == 1:
        if ret:
            cut(b)
        else:
            cut(c)
print('\n'.join(ans))
