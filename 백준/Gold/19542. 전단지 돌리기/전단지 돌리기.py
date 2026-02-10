import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


N, S, D = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


max_sub_depth = [0] * (N+1)


def dfs1(cur, bef):
    my_depth = 0
    for nxt in g[cur]:
        if nxt == bef:
            continue
        my_depth = max(my_depth, dfs1(nxt, cur)+1)
    max_sub_depth[cur] = my_depth
    return my_depth


def dfs2(cur, bef):
    global ans, D
    for nxt in g[cur]:
        if nxt == bef:
            continue
        if max_sub_depth[nxt] >= D:
            ans += 1
            dfs2(nxt, cur)
            ans += 1


dfs1(S, 0)
ans = 0
dfs2(S, 0)
print(ans)