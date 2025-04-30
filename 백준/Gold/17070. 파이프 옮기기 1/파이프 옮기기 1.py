import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# [방향][x][y]
visited = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(3)]
visited[0][1][2] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if board[i-1][j-1]:
            continue
        if j-1 >= 1:
            visited[0][i][j] += (visited[0][i][j-1] + visited[2][i][j-1])
        if i-1 >= 1:
            visited[1][i][j] += (visited[1][i-1][j] + visited[2][i-1][j])
        if i-1 >= 1 and j-1 >= 1:
            if board[i-2][j-1] == 0 and board[i-1][j-2] == 0:
                visited[2][i][j] += (visited[0][i-1][j-1] + visited[1][i-1][j-1] + visited[2][i-1][j-1])


print(visited[0][N][N] + visited[1][N][N] + visited[2][N][N])