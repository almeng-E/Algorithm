import sys
input = sys.stdin.readline


N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
XX = list(map(int, input().split()))

for X in XX:
    N = len(board)
    M = len(board[0])
    if X == 1:
        ans = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                ans[N-1-i][j] = board[i][j]
    elif X == 2:
        ans = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                ans[i][M-1-j] = board[i][j]
    elif X == 3:
        ans = []
        for j in range(M):
            ans.append([])
            for i in range(N-1, -1, -1):
                ans[-1].append(board[i][j])
    elif X == 4:
        ans = []
        for j in range(M-1, -1, -1):
            ans.append([])
            for i in range(N):
                ans[-1].append(board[i][j])
    elif X == 5:
        ans = [[0] * M for _ in range(N)]
        for i in range(N//2):
            for j in range(M//2):
                ans[i][j+M//2] = board[i][j]
        for i in range(N//2):
            for j in range(M//2, M):
                ans[i+N//2][j] = board[i][j]
        for i in range(N//2, N):
            for j in range(M//2, M):
                ans[i][j-M//2] = board[i][j]
        for i in range(N//2, N):
            for j in range(M//2):
                ans[i-N//2][j] = board[i][j]
    else:
        ans = [[0] * M for _ in range(N)]
        for i in range(N//2):
            for j in range(M//2):
                ans[i+N//2][j] = board[i][j]
        for i in range(N//2):
            for j in range(M//2, M):
                ans[i][j-M//2] = board[i][j]
        for i in range(N//2, N):
            for j in range(M//2, M):
                ans[i-N//2][j] = board[i][j]
        for i in range(N//2, N):
            for j in range(M//2):
                ans[i][j+M//2] = board[i][j]
    board = ans

for r in board:
    print(*r)