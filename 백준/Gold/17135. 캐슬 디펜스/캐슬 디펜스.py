import sys
input = sys.stdin.readline

from itertools import combinations
from collections import deque


def bfs(sx, sy):
    q = deque()
    q.append((sx, sy, 0))
    v = [[0 for _ in range(M)] for _ in range(sx)]

    while q:
        x, y, d = q.popleft()
        if d == D:
            continue

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= sx or ny < 0 or ny >= M or v[nx][ny]:
                continue
            if board[nx][ny] == 1:
                tg.append((nx, ny))
                return
            q.append((nx, ny, d + 1))
            v[nx][ny] = 1


N, M, D = map(int, input().split())
original_board = [list(map(int, input().split())) for _ in range(N)]
delta = ((0, -1), (-1, 0), (0, 1))
ans = 0
nCr = combinations(range(M), 3)
for comb in nCr:
    cnt = 0
    py = [c for c in comb]
    board = [r[:] for r in original_board]

    for px in range(N, 0, -1):
        tg = []
        for sy in py:
            bfs(px, sy)

        for x, y in tg:
            if board[x][y]:
                board[x][y] = 0
                cnt += 1

    ans = max(ans, cnt)
print(ans)