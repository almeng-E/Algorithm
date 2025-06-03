T = int(input())
steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
for TC in range(T):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    di = 0
    v = 1
    x, y = 0, 0
    while v <= N**2:
        board[x][y] = v

        nx, ny = x + steps[di][0], y + steps[di][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny]:
            di += 1
            di %= 4

        x, y = x + steps[di][0], y + steps[di][1]
        v += 1

    print(f'#{TC+1}')
    for row in board:
        print(*row)