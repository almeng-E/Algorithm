
def ladder(board):
    # 2 체크
    for i in range(100):
        if board[99][i] == 2:
            x, y = 99, i
            break
    # 실행 부분
    while True:
        x, y, direction = go_up(board, x, y)

        if x == 0:
            return y

        x, y = go_side(board, x, y, direction)


def go_up(board, x, y):
    global check_side
    while True:
        if x == 0:
            return x, y, -1

        for dx, dy, di in check_side:
            if 0 <= y + dy < 100 and board[x][y + dy] == 1:
                return x, y, di
        x -= 1


def go_side(board, x, y, direction):
    if direction == 0:
        dx, dy = 0, -1
    else:
        dx, dy = 0, +1
    while True:
        if 0 <= y + dy < 100 and board[x][y + dy] == 1:
            y = y + dy
        else:
            return x-1, y



#            좌 체크       우 체크
check_side = ((0, -1, 0), (0, +1, +1))


for _ in range(10):
    TC = int(input())

    board = [list(map(int, input().split())) for _ in range(100)]
    result = ladder(board)
    print(f'#{TC} {result}')

