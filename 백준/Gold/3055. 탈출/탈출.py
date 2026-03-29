import sys
input = sys.stdin.readline

from collections import deque

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
steps = ((0, 1), (1, 0), (-1, 0), (0, -1))
sx, sy = -1, -1
water = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            sx, sy = i, j
        elif board[i][j] == '*':
            water.append((i, j))
INF = R*C
W = [[INF for _ in range(C)] for _ in range(R)]
q = deque()
for i, j in water:
    W[i][j] = 0
    q.append((i, j, 0))
while q:
    x, y, t = q.popleft()
    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= R or ny < 0 or ny >= C or board[nx][ny] == 'X' or board[nx][ny] == 'D' or W[nx][ny] <= t+1:
            continue
        W[nx][ny] = t+1
        q.append((nx, ny, t+1))


V = [[0 for _ in range(C)] for _ in range(R)]
q = deque()
q.append((sx, sy, 0))
V[sx][sy] = 1
while q:
    x, y, t = q.popleft()
    if board[x][y] == 'D':
        print(t)
        break
    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= R or ny < 0 or ny >= C or board[nx][ny] == 'X' or W[nx][ny] <= t+1 or V[nx][ny]:
            continue
        V[nx][ny] = 1
        q.append((nx, ny, t+1))
else:
    print('KAKTUS')