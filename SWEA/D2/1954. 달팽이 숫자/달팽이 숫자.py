def snail(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    #       우       하       좌       상
    steps = ((0, +1), (+1, 0), (0, -1), (-1, 0))

    cnt = 1
    curr_x, curr_y = 0, 0
    while True:
       # 이동
        for dx, dy in steps:
            while True:
                board[curr_x][curr_y] = cnt
                if cnt >= N**2:
                    return board
                if 0 <= curr_x + dx < N and 0 <= curr_y + dy < N and board[curr_x + dx][curr_y + dy] == 0:
                    curr_x, curr_y = curr_x + dx, curr_y + dy
                    cnt += 1
                else:
                    break



T = int(input())
for TC in range(T):
    N = int(input())
    board = snail(N)


    print(f'#{TC+1}')
    for i in range(len(board)):
        print(*board[i])
