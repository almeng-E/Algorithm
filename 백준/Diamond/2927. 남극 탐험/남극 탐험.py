import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find(x, p):
    if p[x] != x:
        p[x] = find(p[x], p)
    return p[x]


def union(a, b, p):
    p[a] = b


def dfs1(cur, bef):
    p[cur] = bef
    dep[cur] = dep[bef] + 1
    m_sz = 0
    for nxt in g[cur]:
        if nxt == bef:
            continue
        sz[cur] += dfs1(nxt, cur)
        if m_sz < sz[nxt]:
            m_sz = sz[nxt]
            h_child[cur] = nxt
    return sz[cur]


def dfs2(cur, bef):
    global cnt
    in_[cur] = cnt
    cnt += 1
    if h_child[cur]:
        nxt = h_child[cur]
        head[nxt] = head[cur]
        dfs2(nxt, cur)
    for nxt in g[cur]:
        if nxt == bef or nxt == h_child[cur]:
            continue
        head[nxt] = nxt
        dfs2(nxt, cur)


def excursion(a, b):
    ret = 0
    while head[a] != head[b]:
        if dep[head[a]] > dep[head[b]]:
            a, b = b, a
        l = in_[head[b]] + LEN
        r = in_[b] + LEN
        while l <= r:
            if l & 1:
                ret += tree[l]
                l += 1
            if not (r & 1):
                ret += tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        b = p[head[b]]
    if dep[a] > dep[b]:
        a, b = b, a
    l = in_[a] + LEN
    r = in_[b] + LEN
    while l <= r:
        if l & 1:
            ret += tree[l]
            l += 1
        if not (r & 1):
            ret += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    return ret

N = int(input())
PENGUINS = [0] + list(map(int, input().split()))
Q = int(input())
u_query = []
QUERY = []
for _ in range(Q):
    cmd = input().split()
    a, b = map(int, cmd[1:])
    if cmd[0][0] == 'b':
        QUERY.append((0, a, b))
        u_query.append((a, b))
    elif cmd[0][0] == 'p':
        QUERY.append((1, a, b))
    else:
        QUERY.append((2, a, b))

off_p = [i for i in range(N+1)]
g = [[] for _ in range(N+1)]

for a, b in u_query:
    rt_a = find(a, off_p)
    rt_b = find(b, off_p)
    if rt_a != rt_b:
        union(rt_a, rt_b, off_p)
        g[a].append(b)
        g[b].append(a)

for i in range(1, N+1):
    if off_p[i] == i:
        g[0].append(i)  # 가상의 루트 0
        g[i].append(0)


p = [0] * (N+2)
dep = [0] * (N+2)
sz = [1] * (N+2)
h_child = [0] * (N+2)

head = [0] * (N+2)
in_ = [0] * (N+2)

dfs1(0, -1)
head[0] = 0
cnt = 0
dfs2(0, -1)


LEN = 1
while LEN < N+1:
    LEN <<= 1

tree = [0] * (LEN << 1)
for i in range(N+1):
    tree[in_[i] + LEN] = PENGUINS[i]
for i in range(LEN-1, -1, -1):
    tree[i] = tree[i<<1] + tree[i<<1 | 1]

online_p = [i for i in range(N+1)]

ans = []
for cmd, a, b in QUERY:
    if cmd == 0:
        rt_a = find(a, online_p)
        rt_b = find(b, online_p)
        if rt_a == rt_b:
            ans.append('no')
        else:
            ans.append('yes')
            union(rt_a, rt_b, online_p)

    elif cmd == 1:
        idx = in_[a] + LEN
        tree[idx] = b
        idx >>= 1
        while idx:
            tree[idx] = tree[idx<<1] + tree[idx<<1 | 1]
            idx >>= 1
    else:
        rt_a = find(a, online_p)
        rt_b = find(b, online_p)
        if rt_a == rt_b:
            ans.append(excursion(a, b))
        else:
            ans.append('impossible')

print('\n'.join(map(str, ans)))


