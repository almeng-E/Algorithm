import sys
input = sys.stdin.readline
from collections import deque

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
STEPS = ((0, 1), (0, -1), (1, 0), (-1, 0))
q = deque()
q.append((0, 0))
v = [[float('inf') for _ in range(M)] for _ in range(N)]
v[0][0] = 0
GRAM_DIST = float('inf')
while q:
    x, y = q.popleft()
    for dx, dy in STEPS:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == 1:
            continue
        if v[nx][ny] <= v[x][y] + 1:
            continue

        if board[nx][ny] == 2:
            GRAM_DIST = v[x][y]+1 + N-1-nx+M-1-ny
        v[nx][ny] = v[x][y] + 1
        q.append((nx, ny))

res = min(v[N-1][M-1], GRAM_DIST)
print(res if res <= T else 'Fail')