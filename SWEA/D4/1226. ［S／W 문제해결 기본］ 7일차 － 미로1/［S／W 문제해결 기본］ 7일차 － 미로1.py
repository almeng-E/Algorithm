from collections import deque


steps = ((+1, 0), (-1, 0), (0, +1), (0, -1))


for _ in range(10):
    TC = int(input())

    board = [list(map(int, input())) for _ in range(16)]

    # 시작 위치 찾기
    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                sx, sy = i, j
            if board[i][j] == 3:
                ex, ey = i, j

    res = 0

    queue = deque()
    queue.append((sx, sy))
    while queue:
        x, y = queue.popleft()
        board[x][y] = 1


        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if nx in (-1, 16) or ny in (-1, 16): continue
            if board[nx][ny] == 1: continue

            if board[nx][ny] == 3:
                res = 1
                break
            queue.append((nx, ny))

    print(f'#{TC} {res}')