import sys
input = sys.stdin.readline

def solve(tc):
    board = []
    for i in range(0, 9, 3):
        board.append(tc[i:i + 3])
    xcnt = 0
    ocnt = 0
    xwin = 0
    owin = 0
    for row in board:
        for i in row:
            if i == 'X':
                xcnt += 1
            elif i == 'O':
                ocnt += 1
        if row == 'XXX':
            xwin += 1
        elif row == 'OOO':
            owin += 1
    for j in range(3):
        if board[0][j] + board[1][j] + board[2][j] == 'XXX':
            xwin += 1
        elif board[0][j] + board[1][j] + board[2][j] == 'OOO':
            owin += 1
    if board[0][0] + board[1][1] + board[2][2] == 'XXX':
        xwin += 1
    elif board[0][0] + board[1][1] + board[2][2] == 'OOO':
        owin += 1

    if board[2][0] + board[1][1] + board[0][2] == 'XXX':
        xwin += 1
    elif board[2][0] + board[1][1] + board[0][2] == 'OOO':
        owin += 1

    # 개수 out
    if not (xcnt == ocnt or xcnt == ocnt + 1):
        return 0
    # 승패 안남
    if xcnt + ocnt != 9 and xwin + owin == 0:
        return 0
    # 둘다 승
    if owin > 0 and xwin > 0:
        return 0
    if owin > 0 and xcnt != ocnt:
        return 0
    if xwin > 0 and xcnt == ocnt:
        return 0

    return 1


while True:
    tc = input().rstrip()
    if tc[0] == 'e':
        break
    print(['in', ''][solve(tc)]+'valid')