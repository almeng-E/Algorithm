import sys
input = sys.stdin.readline

from heapq import heappop, heappush


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

steps = ((0, 1), (1, 0), (0, -1), (-1, 0))

hq = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            heappush(hq, (board[i][j], i, j))

for _ in range(S):
    nq = []
    while hq:
        v, x, y = heappop(hq)
        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != 0:
                continue
            board[nx][ny] = v
            heappush(nq, (v, nx, ny))
    hq = nq

print(board[X-1][Y-1])