import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


disc = [0] * (V+1)
low = [0] * (V+1)
uuid = 1
visited = [0] * (V+1)

bridge = []


def dfs(cur, bef):
    global uuid
    visited[cur] = 1
    disc[cur] = uuid
    low[cur] = uuid
    uuid += 1

    for nxt in graph[cur]:
        if nxt == bef:
            continue
        if not visited[nxt]:
            dfs(nxt, cur)

            low[cur] = min(low[cur], low[nxt])

            if disc[cur] < low[nxt]:
                bridge.append((sorted([cur, nxt])))

        else:
            low[cur] = min(low[cur], low[nxt])


for i in range(1, V+1):
    if not visited[i]:
        dfs(i, -1)


print(len(bridge))
for edge in sorted(bridge):
    print(*edge)