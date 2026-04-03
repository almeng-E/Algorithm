import sys
input = sys.stdin.readline
from collections import deque

def forward(x, y, d, mc):
    nx, ny = x + steps[d][0], y + steps[d][1]
    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != '*' and v[nx][ny][d] > mc:
        v[nx][ny][d] = mc
        q.appendleft((mc, nx, ny, d))


def turn(x, y, d, mc):
    for nd in [d+1, d-1]:
        nd %= 4
        nx, ny = x+steps[nd][0], y+steps[nd][1]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != '*' and v[nx][ny][nd] > mc + 1:
            v[nx][ny][nd] = mc+1
            q.append((mc+1, nx, ny, nd))


N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
sx, sy, ex, ey = N, N, N, N

steps = ((0, 1), (-1, 0), (0, -1), (1, 0))

for i in range(N):
    for j in range(N):
        if board[i][j] == '#':
            if sx == N:
                sx, sy = i, j
            else:
                ex, ey = i, j

# v[x][y][d]
v = [[[float('inf') for _ in range(4)] for _ in range(N)] for _ in range(N)]
q = deque()
for i in range(4):
    dx, dy = steps[i]
    nx, ny = sx+dx, sy+dy
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == '*':
        continue
    q.append((0, nx, ny, i))
    v[nx][ny][i] = 0

while q:
    mc, x, y, d = q.popleft()
    if v[x][y][d] < mc:
        continue
    if x == ex and y == ey:
        break

    if board[x][y] == '.':
        forward(x, y, d, mc)
    elif board[x][y] == '!':
        forward(x, y, d, mc)
        turn(x, y, d, mc)

ans = float('inf')
for i in range(4):
    ans = min(ans, v[ex][ey][i])
print(ans)
