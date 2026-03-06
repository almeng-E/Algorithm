import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(cur):
    global timer
    tin[cur] = timer
    timer += 1
    for nxt in g[cur]:
        dep[nxt] = dep[cur] + 1
        dfs(nxt)
    tout[cur] = timer - 1


def range_update(node, s, e, ts, te, v):
    if e < ts or te < s:
        return
    if ts <= s and e <= te:
        tree[node] += v
        return
    mid = (s+e) >> 1
    lc = node << 1
    rc = lc | 1
    range_update(lc, s, mid, ts, te, v)
    range_update(rc, mid+1, e, ts, te, v)


def point_get(node, s, e, tg):
    if s == e:
        return tree[node]
    mid = (s+e) >> 1
    if tg <= mid:
        return tree[node] + point_get(node*2, s, mid, tg)
    else:
        return tree[node] + point_get(node*2 + 1, mid+1, e, tg)


N = int(input())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    g[a].append(b)

dep = [0] * (N + 1)
tin = [0] * (N + 1)
tout = [0] * (N + 1)
timer = 0

dfs(1)

LEN = 1
while LEN < N:
    LEN <<= 1
tree = [0] * (LEN << 1)

ans = []
M = int(input())
for _ in range(N+M-1):
    cmd = input().split()
    if cmd[0] == 'A':
        a = int(cmd[1])
        b = int(cmd[2])
        if dep[a] > dep[b]:
            child = a
        else:
            child = b
        range_update(1, 0, LEN-1, tin[child], tout[child], -1)

    else:
        a = int(cmd[1])
        ans.append(dep[a] + point_get(1, 0, LEN-1, tin[a]))

print('\n'.join(map(str, ans)))