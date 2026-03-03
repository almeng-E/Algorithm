import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 내가 그동안 작성한 lazy의 push down이 비교적 느린 형태임을 학습한 문제
# 원래 : lazy[node]값이 있으면 tree[node]는 최신화 x -> push down해서 최신화하고 자식 전파
# 수정 : tree[node]는 항상 최신값, lazy[node]는 자식에게 미뤄줄 값 저장

# % MOD 말고 & MASK 방법도 있다는걸 배운 문제


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
    out_[cur] = cnt - 1


# lazy를 다르게 보기 -> tree는 항상 최신, lazy는 자식에게 줄 값을 갖고있기
def push_down(node, s, e):
    if m_lazy[node] == 1 and a_lazy[node] == 0:
        return

    if s != e:
        lc = node << 1
        rc = lc | 1
        mid = (s+e) >> 1

        m_lazy[lc] = (m_lazy[lc] * m_lazy[node]) & MOD
        a_lazy[lc] = (a_lazy[lc] * m_lazy[node] + a_lazy[node]) & MOD
        tree[lc] = (tree[lc] * m_lazy[node] + a_lazy[node] * (mid - s + 1)) & MOD

        m_lazy[rc] = (m_lazy[rc] * m_lazy[node]) & MOD
        a_lazy[rc] = (a_lazy[rc] * m_lazy[node] + a_lazy[node]) & MOD
        tree[rc] = (tree[rc] * m_lazy[node] + a_lazy[node] * (e - mid)) & MOD
    m_lazy[node] = 1
    a_lazy[node] = 0


def range_add(node, s, e, ts, te, v):
    if e < ts or te < s:
        return
    if ts <= s and e <= te:
        tree[node] = (tree[node] + v * (e-s+1)) & MOD
        a_lazy[node] = (a_lazy[node] + v) & MOD
        return

    # 자식에게 내려갈 때만 밀어내기
    push_down(node, s, e)

    lc = node << 1
    rc = lc | 1
    mid = (s+e) >> 1
    range_add(lc, s, mid, ts, te, v)
    range_add(rc, mid+1, e, ts, te, v)

    tree[node] = (tree[lc] + tree[rc]) & MOD


def range_mul(node, s, e, ts, te, v):
    if e < ts or te < s:
        return
    if ts <= s and e <= te:
        tree[node] = (tree[node] * v) & MOD
        m_lazy[node] = (m_lazy[node] * v) & MOD
        a_lazy[node] = (a_lazy[node] * v) & MOD
        return

    push_down(node, s, e)

    lc = node << 1
    rc = lc | 1
    mid = (s + e) >> 1
    range_mul(lc, s, mid, ts, te, v)
    range_mul(rc, mid + 1, e, ts, te, v)

    tree[node] = (tree[lc] + tree[rc]) & MOD


def range_get(node, s, e, ts, te):
    if e < ts or te < s:
        return 0

    if ts <= s and e <= te:
        return tree[node]

    push_down(node, s, e)
    lc = node << 1
    rc = lc | 1
    mid = (s + e) >> 1

    return (range_get(lc, s, mid, ts, te) + range_get(rc, mid + 1, e, ts, te)) & MOD


def lca_add(a, b, v):
    while head[a] != head[b]:
        if dep[head[a]] > dep[head[b]]:
            a, b = b, a
        ts, te = in_[head[b]], in_[b]
        range_add(1, 0, LEN-1, ts, te, v)

        b = p[head[b]]

    if dep[a] > dep[b]:
        a, b = b, a
    ts, te = in_[a], in_[b]
    range_add(1, 0, LEN-1, ts, te, v)


def lca_mul(a, b, v):
    while head[a] != head[b]:
        if dep[head[a]] > dep[head[b]]:
            a, b = b, a
        ts, te = in_[head[b]], in_[b]
        range_mul(1, 0, LEN-1, ts, te, v)
        b = p[head[b]]

    if dep[a] > dep[b]:
        a, b = b, a
    ts, te = in_[a], in_[b]
    range_mul(1, 0, LEN-1, ts, te, v)


def lca_get(a, b):
    ret = 0
    while head[a] != head[b]:
        if dep[head[a]] > dep[head[b]]:
            a, b = b, a
        ts, te = in_[head[b]], in_[b]
        ret = (ret + range_get(1, 0, LEN-1, ts, te)) & MOD

        b = p[head[b]]

    if dep[a] > dep[b]:
        a, b = b, a
    ts, te = in_[a], in_[b]
    ret = (ret + range_get(1, 0, LEN-1, ts, te)) & MOD
    return ret

MOD = 0xFFFFFFFF
N, Q = map(int, input().split())
g = [[] for _ in range(N+1)]

p = [0] * (N+1)
dep = [0] * (N+1)
sz = [1] * (N+1)
h_ch = [0] * (N+1)

head = [0] * (N+1)
in_ = [0] * (N+1)
out_ = [0] * (N+1)

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
SIZE = LEN << 1


tree = [0] * SIZE
m_lazy = [1] * SIZE
a_lazy = [0] * SIZE

ans = []
for _ in range(Q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        x, v = cmd[1:]
        v &= MOD
        range_add(1, 0, LEN-1, in_[x], out_[x], v)

    elif cmd[0] == 2:
        x, y, v = cmd[1:]
        v &= MOD
        lca_add(x, y, v)

    elif cmd[0] == 3:
        x, v = cmd[1:]
        v &= MOD
        range_mul(1, 0, LEN-1, in_[x], out_[x], v)

    elif cmd[0] == 4:
        x, y, v = cmd[1:]
        v &= MOD
        lca_mul(x, y, v)

    elif cmd[0] == 5:
        x = cmd[1]
        ans.append(range_get(1, 0, LEN-1, in_[x], out_[x]))

    else:
        x, y = cmd[1:]
        ans.append(lca_get(x, y))

print('\n'.join(map(str, ans)))




