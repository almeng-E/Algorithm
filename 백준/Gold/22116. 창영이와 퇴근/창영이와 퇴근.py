import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
v = [[INF for _ in range(N)] for _ in range(N)]

steps = ((0, 1), (1, 0), (0, -1), (-1, 0))

hq = []
hq.append((0, 0, 0))
v[0][0] = 0
while hq:
    c, x, y = heappop(hq)
    if v[x][y] < c:
        continue
    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        nc = max(abs(board[nx][ny] - board[x][y]), c)
        if v[nx][ny] > nc:
            v[nx][ny] = nc
            heappush(hq, (nc, nx, ny))

print(v[N-1][N-1])