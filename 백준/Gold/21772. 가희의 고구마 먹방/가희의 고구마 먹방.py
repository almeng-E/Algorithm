import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(r, c):
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'G':
                return i, j


def backtrack(x, y, sp, cur):
    global T, ret, steps, R, C, board
    if sp + T - cur <= ret:
        return
    if cur == T:
        ret = max(ret, sp)
        return
    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if board[nx][ny] == '#':
            continue
        elif board[nx][ny] == 'S':
            board[nx][ny] = '.'
            backtrack(nx, ny, sp+1, cur+1)
            board[nx][ny] = 'S'
        else:
            backtrack(nx, ny, sp, cur+1)


steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
R, C, T = map(int, input().split())
board = [list(input()) for _ in range(R)]

sx, sy = find(R, C)

ret = 0
backtrack(sx, sy, 0, 0)
print(ret)