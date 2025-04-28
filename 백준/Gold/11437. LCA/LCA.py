import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(cur, prv):
    for nxt in graph[cur]:
        if nxt != prv:
            depth[nxt] = depth[cur] + 1
            par[nxt] = cur
            dfs(nxt, cur)


N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [0] * (N+1)
par = [0] * (N+1)

dfs(1, 0)

LOG = N.bit_length()

up = [[0 for _ in range(LOG)] for _ in range(N+1)]
# 0칸 채우기
for i in range(1, N+1):
    up[i][0] = par[i]

# 나머지 칸 채우기
for j in range(1, LOG):
    for i in range(1, N+1):
        mid = up[i][j-1]
        up[i][j] = up[mid][j-1]



M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if depth[a] < depth[b]:
        a, b = b, a
    # a가 더 깊음
    diff = depth[a] - depth[b]
    # 깊은 a를 binary lifting으로 끌고 오기 (큰 점프 부터)
    for i in range(LOG-1, -1, -1):
        if diff & (1 << i):
            a = up[a][i]

    # binary lifting을 다시 진행
    if a!= b:
        for i in range(LOG-1, -1, -1):
            if up[a][i] != up[b][i]:
                a = up[a][i]
                b = up[b][i]
        a = par[a]

    print(a)