def dfs(x, y):
    global res
    if board[x][y] == 3:
        res = 1
        return

    board[x][y] = 1


    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if nx in (-1, 16) or ny in (-1, 16): continue
        if board[nx][ny] == 1: continue

        dfs(nx, ny)
        board[nx][ny] = 0


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
    dfs(sx, sy)
    
    print(f'#{TC} {res}')