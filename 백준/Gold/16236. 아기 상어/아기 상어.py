import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

SIZE = 2
cnt = 0
sx, sy = -1, -1

eaten = [[0] * N for _ in range(N)]
steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
for x in range(N):
    for y in range(N):
        if board[x][y] == 9:
            sx, sy = x, y
            board[x][y] = 0

INF = N*N
ans = 0
while True:
    q = deque()
    q.append((sx, sy, 0))
    v = [[0] * N for _ in range(N)]
    v[sx][sy] = 1
    fd = INF
    fish = []
    while q:
        x, y, d = q.popleft()
        if d+1 > fd:
            continue
        for dx, dy in steps:
            nx, ny, nd = x+dx, y+dy, d+1
            if nx < 0 or nx >= N or ny < 0 or ny >= N or v[nx][ny] or board[nx][ny] > SIZE:
                continue
            # 갈 수 있음
            v[nx][ny] = 1
            if not eaten[nx][ny] and 0 < board[nx][ny] < SIZE:
                if fd > nd:
                    fd = nd
                    fish = [(nx, ny)]
                elif fd == nd:
                    fish.append((nx, ny))
            q.append((nx, ny, nd))

    if not fish:
        break

    fish.sort()
    fx, fy = fish[0]
    ans += fd
    sx, sy = fx, fy
    eaten[fx][fy] = 1
    cnt += 1

    if cnt == SIZE:
        SIZE += 1
        cnt = 0

print(ans)

