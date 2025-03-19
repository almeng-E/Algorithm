import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(c_node, parent):
    visited[c_node] = True

    for n_node in graph[c_node]:
        if not visited[n_node]:
            if not dfs(n_node, c_node):
                return False
        else:
            if parent != n_node:
                return False
    return True


TC = 0
while True:
    TC += 1
    N, M = map(int, input().split())

    if N == 0: break

    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    res = 0
    for v in range(1, N+1):
        if not visited[v]:
            if dfs(v, None):
                res += 1


    # 출력
    print(f'Case {TC}: ', end='')
    if res == 0:
        print('No trees.')
    elif res == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {res} trees.')
