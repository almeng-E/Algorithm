import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(cur):
    global cnt, res
    if res:
        return
    if cnt == 5:
        res = True
        return

    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            cnt += 1
            dfs(nxt)
            visited[nxt] = False
            cnt -= 1

visited = [False] * N

cnt = 0
res = False
for st in range(N):
    visited[st] = True
    cnt += 1
    dfs(st)
    visited[st] = False
    cnt -= 1

print(1 if res else 0)