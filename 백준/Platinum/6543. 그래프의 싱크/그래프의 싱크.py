import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs1(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs1(nxt)
    order.append(cur)


def dfs2(cur):
    visited[cur] = True
    SCC[cur] = _id
    for nxt in r_graph[cur]:
        if not visited[nxt]:
            dfs2(nxt)


while True:
    try:
        N, M = map(int, input().split())
        edges = list(map(int, input().split()))

        graph = [[] for _ in range(N+1)]
        r_graph = [[] for _ in range(N+1)]

        for i in range(0, 2*M, 2):
            a, b = edges[i], edges[i+1]
            graph[a].append(b)
            r_graph[b].append(a)


        order = []
        visited = [False] * (N+1)
        for i in range(1, N+1):
            if not visited[i]:
                dfs1(i)

        visited = [False] * (N+1)
        _id = 1
        SCC = [0] * (N+1)

        for i in reversed(order):
            if not visited[i]:
                dfs2(i)
                _id += 1

        # print(SCC)
        # print(cache)
        out_degree = [0] * _id
        for i in range(0, 2*M, 2):
            a, b = edges[i], edges[i+1]
            if SCC[a] != SCC[b]:
                out_degree[SCC[a]] += 1

        bottom = []
        for i in range(1, N+1):
            _id = SCC[i]
            if out_degree[_id] == 0:
                bottom.append(i)

        bottom.sort()
        print(*bottom)


    except ValueError:
        break