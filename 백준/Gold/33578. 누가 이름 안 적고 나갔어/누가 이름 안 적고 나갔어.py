import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
INF = float('inf')

# J -> S
# T -> S

sx, sy = -1, -1
jx, jy = -1, -1
t = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 'S':
            sx, sy = i, j
        elif board[i][j] == 'J':
            jx, jy = i, j
        elif board[i][j] == 'T':
            t.append((i, j))

dist_j = [[INF for _ in range(M)] for _ in range(N)]
dist_j[jx][jy] = 0
q = deque()
q.append((jx, jy))
while q:
    x, y = q.popleft()
    if (x, y) == (sx, sy):
        break
    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if board[nx][ny] == '#':
            continue
        if dist_j[nx][ny] > dist_j[x][y] + 2:
            dist_j[nx][ny] = dist_j[x][y] + 2
            q.append((nx, ny))


dist_s = [[INF for _ in range(M)] for _ in range(N)]
dist_s[sx][sy] = 0
q = deque()
q.append((sx, sy))
cnt = 0
while q:
    x, y = q.popleft()
    if board[x][y] == 'T':
        cnt += 1
    if cnt == len(t):
        break
    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if board[nx][ny] == '#':
            continue
        if dist_s[nx][ny] > dist_s[x][y] + 1:
            dist_s[nx][ny] = dist_s[x][y] + 1
            q.append((nx, ny))

res = dist_j[sx][sy]
for tx, ty in t:
    res = min(res, dist_j[tx][ty] + dist_s[tx][ty])
print(res if res != INF else -1)