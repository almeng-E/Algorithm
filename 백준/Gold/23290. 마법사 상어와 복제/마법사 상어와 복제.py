import sys
input = sys.stdin.readline

from collections import deque
from itertools import product

M, S = map(int, input().split())
# board[횟수][x][y] = [d] of fish
board = [[[[] for _ in range(4)] for _ in range(4)] for _ in range(S+1)]

smell = [[deque() for _ in range(4)] for _ in range(4)]

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
steps = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
s_d = (2, 0, 6, 4)

s_moves = list(product(s_d, repeat=3))
for _ in range(M):
    fx, fy, fd = map(int, input().split())
    board[0][fx-1][fy-1].append(fd-1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1
for time in range(S):
    cur = board[time]
    nxt = board[time+1]

    for x in range(4):
        for y in range(4):
            for d in cur[x][y]:
                for k in range(8):
                    nd = (d - k) % 8
                    dx, dy = steps[nd]
                    nx, ny = x+dx, y+dy
                    if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or smell[nx][ny] or (nx, ny) == (sx, sy):
                        continue
                    nxt[nx][ny].append(nd)
                    break
                else:
                    nxt[x][y].append(d)

    cur_max = -1
    max_j = -1

    for j in range(64):
        x, y = sx, sy
        cnt = 0
        visited = set()

        for sd in s_moves[j]:
            dx, dy = steps[sd]
            x += dx
            y += dy
            if x < 0 or x >= 4 or y < 0 or y >= 4:
                break

            if (x, y) not in visited:
                cnt += len(nxt[x][y])
                visited.add((x, y))
        else:
            if cur_max < cnt:
                cur_max = cnt
                max_j = j

    for sd in s_moves[max_j]:
        dx, dy = steps[sd]
        sx += dx
        sy += dy
        if nxt[sx][sy]:
            smell[sx][sy].append(time+1)
            nxt[sx][sy].clear()

    for x in range(4):
        for y in range(4):
            while smell[x][y] and smell[x][y][0] <= time-1:
                smell[x][y].popleft()

    for x in range(4):
        for y in range(4):
            nxt[x][y].extend(cur[x][y])

ans = 0
for x in range(4):
    for y in range(4):
        ans += len(board[S][x][y])

print(ans)
