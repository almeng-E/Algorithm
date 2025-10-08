import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DP = [[-float('inf') for _ in range(M)] for _ in range(N)]

x1, y1, x2, y2 = map(int, input().split())
if (x1 == x2 and y1 == y2) or x1 == x2 == N or y1 == y2 == M or x1 == x2 == 0 or y1 == y2 == 0:
    wdi = -1
else:
    if x1 == x2:
        wdi = 0
        if y1 > y2:
            y1, y2 = y2, y1
    else:
        wdi = 1
        if x1 > x2:
            x1, x2 = x2, x1

steps = ((1, 0), (0, 1))
q = deque()
q.append((0, 0, board[0][0]))
DP[0][0] = board[0][0]

while q:
    x, y, d = q.popleft()
    if d < DP[x][y]:
        continue

    for di in range(2):
        dx, dy = steps[di]
        nx, ny = x + dx, y + dy

        if nx >= N or ny >= M:
            continue

        if wdi == di:
            if wdi == 0 and nx == x1 and y1 <= ny < y2:
                continue
            if wdi == 1 and ny == y1 and x1 <= nx < x2:
                continue

        nd = d + board[nx][ny]
        if DP[nx][ny] < nd:
            DP[nx][ny] = nd
            q.append((nx, ny, nd))

if DP[N-1][M-1] != -float('inf'):
    print(DP[N-1][M-1])
else:
    print('Entity')
