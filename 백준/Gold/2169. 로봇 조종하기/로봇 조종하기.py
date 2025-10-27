import sys
input = sys.stdin.readline
N, M = map(int, input().split())

steps = ((0, -1), (0, 1), (1, 0))
board = [list(map(int, input().split())) for _ in range(N)]
DP = [-float('inf')] * M
DP[0] = board[0][0]
for j in range(1, M):
    DP[j] = DP[j-1] + board[0][j]


for i in range(1, N):
    L = [-float('inf')] * M
    R = [-float('inf')] * M

    # 왼 -> 오
    L[0] = DP[0] + board[i][0]
    for j in range(1, M):
        L[j] = max(L[j - 1], DP[j]) + board[i][j]

    # 오 -> 왼
    R[M - 1] = DP[M - 1] + board[i][M - 1]
    for j in range(M - 2, -1, -1):
        R[j] = max(R[j + 1], DP[j]) + board[i][j]


    for j in range(M):
        DP[j] = max(L[j], R[j])

print(DP[M-1])