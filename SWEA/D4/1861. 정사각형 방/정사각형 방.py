def dfs(x, y, cnt):
    res = cnt

    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        if board[nx][ny] == board[x][y] + 1:
            res = dfs(nx, ny, cnt+1)

    return res

T = int(input())

steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))
for TC in range(T):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    s = 0
    for i in range(N):
        for j in range(N):
            tmp = dfs(i, j, 1)
            if res < tmp:
                res = tmp
                s = board[i][j]
            elif res == tmp:
                if s > board[i][j]:
                    s = board[i][j]


    print(f'#{TC+1} {s} {res}')