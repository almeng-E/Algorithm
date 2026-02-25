import sys
input = sys.stdin.readline

from collections import deque


def puyo(sx, sy):
    tg = board[sx][sy]
    q = deque()
    q.append((sx, sy))
    v[sx][sy] = 1
    tmp = []
    while q:
        x, y = q.popleft()
        tmp.append((x, y))
        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if board[nx][ny] != tg:
                continue
            if not v[nx][ny]:
                v[nx][ny] = 1
                q.append((nx, ny))
    if len(tmp) >= 4:
        for x, y in tmp:
            board[x][y] = '.'
        return 1
    else:
        return 0


def down():
    global board
    nxt = [['.' for _ in range(6)] for _ in range(12)]
    for j in range(6):
        st = []
        for i in range(11, -1, -1):
            if board[i][j] != '.':
                st.append(board[i][j])
        for k in range(len(st)):
            nxt[11-k][j] = st[k]
    board = nxt


steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
board = [list(input()) for _ in range(12)]
ans = 0
while True:
    ret = 0
    v = [[0 for _ in range(6)] for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not v[i][j]:
                ret += puyo(i, j)
    if ret == 0:
        break
    down()
    ans += 1

print(ans)