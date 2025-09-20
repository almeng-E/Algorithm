import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 코사라주 SCC
def dfs1(cur):
    visited[cur] = True
    for nxt in r_graph[cur]:
        if not visited[nxt]:
            dfs1(nxt)
    v_order.append(cur)


def dfs2(cur):
    global SCC_ID
    visited[cur] = True
    SCC[cur] = SCC_ID
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs2(nxt)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    r_graph = [[] for _ in range(N+1)]
    edges = []

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        edges.append((x, y))
        r_graph[y].append(x)

    # 첫번째 dfs : 다음 순회 순서 정하기
    visited = [False] * (N+1)
    v_order = []

    for i in range(1, N+1):
        if not visited[i]:
            dfs1(i)

    # 두번째 dfs : SCC 루트에서 시작해서, SCC 처리
    visited = [False] * (N+1)
    SCC = [-1] * (N+1)
    SCC_ID = 0

    for i in reversed(v_order):
        if not visited[i]:
            dfs2(i)
            SCC_ID += 1

    # SCC 의 진입 차수 찾기
    SCC_in_degree = [0] * SCC_ID
    for x, y in edges:
        if SCC[x] != SCC[y]:
            SCC_in_degree[SCC[y]] += 1

    res = 0
    for i in range(SCC_ID):
        if SCC_in_degree[i] == 0:
            res += 1

    print(res)