import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs1(cur):
    global g, v, v_order
    nxt = g[cur]
    if not v[nxt]:
        v[nxt] = 1
        dfs1(nxt)
    v_order.append(cur)


def dfs2(cur, root, c):
    global g, v, cnt
    nxt = g[cur]
    if nxt == root:
        cnt += c
        return
    if v[nxt]:
        return
    else:
        v[nxt] = 1
        dfs2(nxt, root, c+1)


T = int(input())
for _ in range(T):
    N = int(input())
    g = [0] + list(map(int, input().split()))
    v = [0] * (N+1)
    v_order = []
    for i in range(1, N+1):
        if not v[i]:
            v[i] = 1
            dfs1(i)
    cnt = 0
    v = [0] * (N+1)
    for i in v_order:
        if not v[i]:
            v[i] = 1
            dfs2(i, i, 1)
    print(N-cnt)