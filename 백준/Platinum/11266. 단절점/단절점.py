import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(cur, bef):
    global CNT, visited, res
    visited[cur] = CNT
    low[cur] = CNT
    children = 0
    CNT += 1
    for nxt in graph[cur]:
        if nxt == bef:
            continue
        if visited[nxt] == -1:
            children += 1
            dfs(nxt, cur)
            low[cur] = min(low[cur], low[nxt])

            if bef != -1 and low[nxt] >= visited[cur]:
                res.add(cur)
        else:
            low[cur] = min(low[cur], visited[nxt])
    if bef == -1 and children >= 2:
        res.add(cur)

CNT = 0

res = set()

visited = [-1] * (V+1)
low = [-1] * (V+1)

# 연결 컴포넌트가 아닐 수 있대
for i in range(1, V+1):
    if visited[i] == -1:
        dfs(i, -1)

print(len(res))
print(*sorted(res))