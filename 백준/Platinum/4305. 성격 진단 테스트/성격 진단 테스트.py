import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs1(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs1(nxt)
    v_order.append(cur)


def dfs2(cur):
    visited[cur] = True
    SCC[cur] = SCC_ID
    SCC_group[SCC_ID].append(cur)
    for nxt in r_graph[cur]:
        if not visited[nxt]:
            dfs2(nxt)


while True:
    N = int(input())
    if N == 0:
        break
    graph = [[] for _ in range(26)]
    r_graph = [[] for _ in range(26)]
    used = [False] * 26
    for _ in range(N):
        line = input().split()
        a = line[5]
        used[ord(a)-65] = True
        for i in range(5):
            b = line[i]
            if a == b:
                continue
            used[ord(b) - 65] = True
            graph[ord(a)-65].append(ord(b)-65)
            r_graph[ord(b)-65].append(ord(a)-65)


    visited = [False] * 26
    v_order = []
    for i in range(26):
        if used[i] and not visited[i]:
            dfs1(i)


    visited = [False] * 26
    SCC = [-1] * 26
    SCC_ID = 0
    SCC_group = []

    for i in reversed(v_order):
        if used[i] and not visited[i]:
            SCC_group.append([])
            dfs2(i)
            SCC_ID += 1

    for row in SCC_group:
        row.sort()
    SCC_group.sort(key=lambda x: x[0])
    for row in SCC_group:
        for c in row:
            print(chr(c+65), end=" ")
        print()
    print()