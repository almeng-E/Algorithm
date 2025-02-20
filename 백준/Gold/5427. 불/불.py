from collections import deque


steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))

T = int(input())

for _ in range(T):
    W, H = map(int, input().split())

    board = [list(input()) for _ in range(H)]

    # 불 번지기
    fire_time = [[-1 for _ in range(W)] for _ in range(H)]
    f_queue = deque()
    s_queue = deque()
    # 위치 찾기
    for i in range(H):
        for j in range(W):
            if board[i][j] == '*':
                f_queue.append((i, j))
                fire_time[i][j] = 0
            if board[i][j] == '@':
                s_queue.append((i, j))
                board[i][j] = 0

    while f_queue:
        x, y = f_queue.popleft()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < H and 0 <= ny < W): continue
            if board[nx][ny] == '#': continue

            if board[nx][ny] != '*' and fire_time[nx][ny] == -1:
                f_queue.append((nx, ny))
                fire_time[nx][ny] = fire_time[x][y] + 1
    res = 0
    while s_queue:
        x, y = s_queue.popleft()
        if x in (0, H-1) or y in (0, W-1):
            res = board[x][y] + 1
            break

        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < H and 0 <= ny < W): continue
            if board[nx][ny] != '.': continue

            if board[nx][ny] == '.' and (fire_time[nx][ny] == -1 or fire_time[nx][ny] > board[x][y] + 1):
                s_queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1

    print('IMPOSSIBLE' if res==0 else res)