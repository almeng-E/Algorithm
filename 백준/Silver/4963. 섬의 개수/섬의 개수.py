from collections import deque

steps = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
while True:
    w, h = map(int, input().split())
    if w == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] != 1:
                continue
            cnt += 1

            q = deque()
            q.append((i, j))
            board[i][j] = -1

            while q:
                x, y = q.popleft()
                for dx, dy in steps:
                    nx, ny = x+dx, y+dy
                    if 0 > nx or nx >= h or 0 > ny or ny >= w:
                        continue
                    if board[nx][ny] == 1:
                        board[nx][ny] = -1
                        q.append((nx, ny))

    print(cnt)