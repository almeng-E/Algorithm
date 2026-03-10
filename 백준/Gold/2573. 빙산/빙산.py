import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
steps = ((0, 1), (1, 0), (0, -1), (-1, 0))

ans = 0
while True:
    v = [[0] * M for _ in range(N)]
    g_cnt = 0
    ice = []
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and v[i][j] == 0:
                g_cnt += 1
                q = deque()
                v[i][j] = g_cnt
                ice.append((i, j))
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for dx, dy in steps:
                        nx, ny = x + dx, y + dy
                        if nx == 0 or nx == N or ny == 0 or ny == M:
                            continue
                        if board[nx][ny] != 0 and v[nx][ny] == 0:
                            v[nx][ny] = g_cnt
                            q.append((nx, ny))
                            ice.append((nx, ny))
    if g_cnt >= 2:
        break
    elif g_cnt == 0:
        ans = 0
        break

    melt = []
    for x, y in ice:
        cnt = 0
        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                cnt += 1
        melt.append(cnt)

    for i in range(len(ice)):
        x, y = ice[i]
        v = melt[i]
        board[x][y] = max(0, board[x][y]-v)

    ans += 1
print(ans)
