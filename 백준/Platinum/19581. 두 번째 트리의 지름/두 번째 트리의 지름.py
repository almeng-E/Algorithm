import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))


def dfs(cur, bef, dist):
    global max_dist, max_node
    for nxt, w in graph[cur]:
        if nxt == bef:
            continue
        dfs(nxt, cur, dist + w)
    if max_dist < dist:
        max_dist = dist
        max_node = cur


max_dist = 0
max_node = 1
dfs(1, 0, 0)


def dfs2(cur, bef, dist, no):
    global res
    for nxt, w, in graph[cur]:
        if nxt == bef:
            continue
        if nxt == no:
            continue
        dfs2(nxt, cur, dist + w, no)
    res = max(res, dist)


res = 0
s = max_node
max_dist = 0    # 어우 변수명 지저분해
max_node = 0
dfs(s, 0, 0)

dfs2(s, 0, 0, max_node)
dfs2(max_node, 0, 0, s)


print(res)
