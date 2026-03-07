import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs1(cur):
    dep[cur] = dep[p[cur]] + 1
    m_sz = 0
    for nxt in g[cur]:
        sz[cur] += dfs1(nxt)
        if m_sz < sz[nxt]:
            m_sz = sz[nxt]
            h_ch[cur] = nxt
    return sz[cur]


def dfs2(cur):
    global cnt
    in_[cur] = cnt
    cnt += 1
    if h_ch[cur]:
        nxt = h_ch[cur]
        head[nxt] = head[cur]
        dfs2(nxt)
    for nxt in g[cur]:
        if nxt == h_ch[cur]:
            continue
        head[nxt] = nxt
        dfs2(nxt)


def query(a, b):
    ret = -1
    while head[a] != head[b]:
        if dep[head[a]] > dep[head[b]]:
            a, b = b, a
        ret += (in_[b] - in_[head[b]] + 1)
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
    ret += (in_[b] - in_[a] + 1)
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

    ret -= tree[in_[a] + LEN]

    return ret


N = int(input())
g = [[] for _ in range(N+1)]
p = [0] * (N+1)
arr = list(map(int, input().split()))
for i in range(N-1):
    x = arr[i]
    g[x].append(i+2)
    p[i+2] = x


dep = [0] * (N+1)
sz = [1] * (N+1)
h_ch = [0] * (N+1)

head = [0] * (N+1)
in_ = [0] * (N+1)

dfs1(1)
head[1] = 1
cnt = 0
dfs2(1)

LEN = 1
while LEN < N:
    LEN <<= 1
tree = [0] * (LEN*2)

ans = []
Q = int(input())
for _ in range(Q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        a, b = cmd[1:]
        ans.append(query(a, b))

    else:
        v = cmd[1]
        idx = in_[v] + LEN
        while idx:
            tree[idx] -= 1
            idx >>= 1

print('\n'.join(map(str, ans)))
