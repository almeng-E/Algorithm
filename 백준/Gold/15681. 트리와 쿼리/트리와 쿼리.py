import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(node):
    global ROOT
    if len(graph[node]) == 1 and node != ROOT:
        sub_cnt[node] = 1
        return sub_cnt[node]

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            sub_cnt[node] += dfs(next_node)

    return sub_cnt[node]


N, ROOT, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

sub_cnt = [1] * (N+1)
visited = [False] * (N+1)
visited[ROOT] = True
dfs(ROOT)
for _ in range(Q):
    print(sub_cnt[int(input())])