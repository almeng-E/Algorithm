import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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
    tmp.append(cur)
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs2(nxt)



# 코사라주 SCC
T = int(input())
for tc in range(T):
    if tc != 0:
        _ = input()
        print()

    N, M = map(int, input().split())

    graph = [[] for _ in range(N)]
    r_graph = [[] for _ in range(N)]
    edges = []

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        r_graph[b].append(a)
        edges.append((a, b))

    # 1차 DFS : 루트 찾기
    visited = [False] * N
    v_order = []
    for i in range(N):
        if not visited[i]:
            dfs1(i)


    # 2차 DFS : SCC 찾기
    visited = [False] * N
    SCC_ID = 0
    SCC = [-1] * N
    SCC_nodes = []
    for i in reversed(v_order):
        if not visited[i]:
            tmp = []
            dfs2(i)
            SCC_nodes.append(tmp)
            SCC_ID += 1

    # SCC 진입차수 찾기
    STARTING_SCC = set(i for i in range(SCC_ID))
    for a, b in edges:
        if SCC[a] != SCC[b]:
            if SCC[b] in STARTING_SCC:
                STARTING_SCC.remove(SCC[b])
    # 진입차수 0인곳 찾기
    if len(STARTING_SCC) == 1:
        res = STARTING_SCC.pop()
        for i in sorted(SCC_nodes[res]):
            print(i)
    else:
        print("Confused")