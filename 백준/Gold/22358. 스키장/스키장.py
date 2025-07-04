import sys
input = sys.stdin.readline
N, M, K, S, T = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
INF = float('inf')
DP = [[-INF for _ in range(N+1)] for _ in range(K+1)] # [남은횟수][번호]

DP[K][S] = 0

for i in range(K, -1, -1):

    # DFS
    for cur in range(1, N+1):
        for nxt, w in graph[cur]:
            if DP[i][nxt] < DP[i][cur] + w:
                DP[i][nxt] = DP[i][cur] + w

    # 업 ... 최적화 가능?
    if i > 0:
        for j in range(1, N+1):
            for nxt, _ in graph[j]:
                DP[i-1][j] = max(DP[i-1][j], DP[i][nxt])

res = -1
for i in range(K+1):
    res = max(DP[i][T], res)
print(res)
