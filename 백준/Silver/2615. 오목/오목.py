import sys
input = sys.stdin.readline


def check(i, j, dx, dy, color):
    global board
    cnt = 1
    sx, sy = i, j
    # 정방향 체크
    while True:
        if 0 <= i+dx < 19 and 0 <= j+dy < 19 and board[i+dx][j+dy] == color:
            i, j = i+dx, j+dy
            cnt += 1
            if cnt > 5:
                return False
        else:
            break
    # cnt 체크
    if cnt < 5:
        return False
    elif cnt == 5:
        # 6목 방지 역방향 체크
        if 0 <= sx-dx < 19 and 0 <= sy-dy < 19:
            if board[sx-dx][sy-dy] != color:
                return True
            else:
                return False
        else:
            return True


def omok(board):
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue
            color = board[i][j]

            for dx, dy in steps:
                if check(i, j, dx, dy, color):
                    return (color, i, j)
    return (0, 0, 0)


board = [list(map(int, input().split())) for _ in range(19)]

         #  ㅡ        |        /         \
steps = ((0, +1), (+1, 0), (-1, +1), (+1, +1))

a, b, c = omok(board)
if a == 0:
    print(0)
else:
    print(a)
    print(b+1, c+1)

