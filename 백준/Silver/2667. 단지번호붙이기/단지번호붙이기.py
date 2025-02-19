import sys

sys.setrecursionlimit(10**6)

def dfs(x, y):
    global board, tmp
    board[x][y] = 0
    tmp += 1

    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx in (-1, N) or ny in (-1, N):
            continue
        if board[nx][ny] == 0:
            continue
        dfs(nx, ny)


steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))
N = int(input())

board = [list(map(int, input())) for _ in range(N)]

res = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            tmp = 0
            dfs(i, j)
            res.append(tmp)

res.sort()
print(len(res))
for i in res:
    print(i)