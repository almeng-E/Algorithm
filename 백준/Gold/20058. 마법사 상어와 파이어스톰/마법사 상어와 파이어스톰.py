import sys
input = sys.stdin.readline
from collections import deque

N, Q = map(int, input().split())
SIZE = 1 << N
board = [list(map(int, input().split())) for _ in range(SIZE)]

L = list(map(int, input().split()))
steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
for q in range(Q):
    l = 1 << L[q]
    new_board = [[0] * SIZE for _ in range(SIZE)]
    for i in range(0, SIZE, l):
        for j in range(0, SIZE, l):
            for r in range(l):
                for c in range(l):
                    new_board[i + c][j + l-1 - r] = board[i + r][j + c]
    board = new_board

    melt_list = []
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] > 0:
                ice_count = 0
                for di, dj in steps:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < SIZE and 0 <= nj < SIZE and board[ni][nj] > 0:
                        ice_count += 1

                if ice_count < 3:
                    melt_list.append((i, j))

    for i, j in melt_list:
        board[i][j] -= 1

v = [[0] * SIZE for _ in range(SIZE)]
ret1 = 0
ret2 = 0
for i in range(SIZE):
    for j in range(SIZE):
        ret1 += board[i][j]
        if v[i][j] or board[i][j] == 0: continue
        q = deque()
        q.append((i, j))
        v[i][j] = 1
        cnt = 1
        while q:
            x, y = q.popleft()
            for dx, dy in steps:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= SIZE or ny < 0 or ny >= SIZE or board[nx][ny] == 0 or v[nx][ny]:
                    continue
                q.append((nx, ny))
                v[nx][ny] = 1
                cnt += 1
        ret2 = max(ret2, cnt)
print(ret1)
print(ret2)
