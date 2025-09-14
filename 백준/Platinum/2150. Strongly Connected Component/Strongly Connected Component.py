import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# 코라사주?
V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
r_graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    r_graph[b].append(a)

# 1차 DFS
visited = [False] * (V+1)
num = [0] * (V+1)
v_cnt = 1
first_num_order = []


def dfs(cur):
    global v_cnt
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)
    # 나올 때 방문 처리
    num[cur] = v_cnt
    v_cnt += 1
    first_num_order.append(cur)

for i in range(1, V+1):
    if not visited[i]:
        dfs(i)


# 두번째 DFS
visited = [False] * (V+1)
res = []


def dfs2(cur):
    SCC.append(cur)
    visited[cur] = True
    for nxt in r_graph[cur]:
        if not visited[nxt]:
            dfs2(nxt)


for i in reversed(first_num_order):
    if not visited[i]:
        SCC = []
        dfs2(i)
        res.append(sorted(SCC))
        res[-1].append(-1)

res.sort(key=lambda x: x[0])
print(len(res))
for scc in res:
    print(*scc)