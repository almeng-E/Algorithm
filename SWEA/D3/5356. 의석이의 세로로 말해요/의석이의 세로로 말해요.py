T = int(input())
for TC in range(T):


    board = [list(input()) for _ in range(5)]
    m = 0
    for i in board:
        if m < len(i):
            m = len(i)
    print(f'#{TC+1} ',end="")
    for j in range(m):
        for i in range(5):
            try:
                print(board[i][j], end="")
            except IndexError:
                continue
    print()