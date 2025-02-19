import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global board
    # 방문
    board[x][y] = 2

    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] != 1:
            continue
        dfs(nx, ny)


steps = ((0, -1), (0, +1), (-1, 0), (+1, 0))

T = int(input())
for _ in range(T):
    # M : 가로, N : 세로, K : 배추 개수
    # N x M 보드
    M, N, K = map(int, input().split())

    board = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    res = 0
    # 그룹 개수 세기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                dfs(i, j)
                res += 1
    print(res)