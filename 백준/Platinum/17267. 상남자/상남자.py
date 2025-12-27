import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
L, R = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
sx, sy = -1, -1

def solve():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                sx, sy = i, j
                break

    v = [[0] * M for _ in range(N)]
    v[sx][sy] = 1
    res = 1
    q = deque()
    q.append((sx, sy, L, R))
    while q:
        x, y, l, r = q.popleft()

        # 좌
        if l > 0 and y-1 >= 0 and board[x][y-1] == 0 and v[x][y-1] == 0:
            q.append((x, y-1, l-1, r))
            v[x][y-1] = 1
            res += 1
        # 우
        if r > 0 and y+1 < M and board[x][y+1] == 0 and v[x][y+1] == 0:
            q.append((x, y+1, l, r-1))
            v[x][y+1] = 1
            res += 1
        # 상
        nx = x
        while nx >= 0:
            if board[nx][y] == 0 and v[nx][y] == 0:
                q.append((nx, y, l, r))
                v[nx][y] = 1
                res += 1
            elif board[nx][y] == 1:
                break
            nx -= 1

        # 하
        nx = x
        while nx < N:
            if board[nx][y] == 0 and v[nx][y] == 0:
                q.append((nx, y, l, r))
                v[nx][y] = 1
                res += 1
            elif board[nx][y] == 1:
                break
            nx += 1
    print(res)

solve()
