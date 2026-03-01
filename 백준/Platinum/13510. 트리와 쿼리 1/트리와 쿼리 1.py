import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 전처리 : p, depth, size, weight, heavy
def dfs1(cur, bef):
    p[cur] = bef
    depth[cur] = depth[bef] + 1

    max_size = 0
    for nxt, w in g[cur]:
        if nxt == bef:
            continue
        weight[nxt] = w
        size[cur] += dfs1(nxt, cur)
        if max_size < size[nxt]:
            max_size = size[nxt]
            heavy[cur] = nxt

    return size[cur]


# HLD 전처리 : head, in_
def dfs2(cur, bef):
    global cnt
    in_[cur] = cnt
    cnt += 1
    if heavy[cur]:
        nxt = heavy[cur]
        head[nxt] = head[cur]
        dfs2(nxt, cur)
    for nxt, w in g[cur]:
        if nxt != bef and nxt != heavy[cur]:
            head[nxt] = nxt
            dfs2(nxt, cur)


# 트리 조회
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


N = int(input())

edges = [[]]            # index 저장용
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))
    edges.append([u, v])

p = [0] * (N+1)         # 부모
depth = [0] * (N+1)     # 깊이
size = [1] * (N+1)      # 서브트리의 크기
weight = [0] * (N+1)    # 가중치 저장
heavy = [0] * (N+1)     # heavy child

head = [0] * (N+1)      # 체인의 가장 위 노드
in_ = [0] * (N+1)       # OTT

depth[0] = -1
dfs1(1, 0)

cnt = 0
head[1] = 1
dfs2(1, 0)

LEN = 1
while LEN < N:
    LEN <<= 1
tree = [0] * (LEN << 1)

for i in range(N+1):
    tree[in_[i]+LEN] = weight[i]
for i in range(LEN-1, 0, -1):
    tree[i] = max(tree[i*2], tree[i*2 + 1])


M = int(input())
ans = []
for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        i, c = cmd[1:]
        u, v = edges[i]
        if depth[u] < depth[v]:
            node = v
        else:
            node = u
        idx = in_[node] + LEN
        tree[idx] = c
        idx >>= 1
        while idx:
            tree[idx] = max(tree[idx*2], tree[idx*2 + 1])
            idx >>= 1
    else:
        u, v = cmd[1:]
        ret = 0
        while head[u] != head[v]:
            if depth[head[u]] > depth[head[v]]:
                u, v = v, u
            l = in_[head[v]] + LEN
            r = in_[v] + LEN
            ret = max(ret, range_get(l, r))
            v = p[head[v]]

        if depth[u] > depth[v]:
            u, v = v, u
        l = in_[u] + LEN + 1    # 간선 쿼리이니 조심!!
        r = in_[v] + LEN
        ret = max(ret, range_get(l, r))
        ans.append(ret)

print('\n'.join(map(str, ans)))