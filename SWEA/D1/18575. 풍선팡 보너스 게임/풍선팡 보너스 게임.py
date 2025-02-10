def sum_row(i, j, board, N):
    tmp = 0
    for y in range(N):
        tmp += board[i][y]
    return tmp

def sum_col(i, j, board, N):
    tmp = 0
    for x in range(N):
        tmp += board[x][j]
    return tmp

T = int(input())
for TC in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    min_num = 20*20
    for i in range(N):
        for j in range(N):
            a = sum_row(i, j, board, N)
            b = sum_col(i, j, board, N)
            if max_num < a + b - board[i][j]:
                max_num = a + b - board[i][j]
            if min_num > a + b - board[i][j]:
                min_num = a + b - board[i][j]

    print(f'#{TC+1} {max_num - min_num}')
