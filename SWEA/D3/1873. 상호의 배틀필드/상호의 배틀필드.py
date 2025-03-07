def find_current():
    global c_direction
    for i in range(H):
        for j in range(W):
            if board[i][j] in direction_dict.keys():
                c_direction = direction_dict[board[i][j]]
                return i, j


def game(command):
    # 동작 별 구분
    if command == 'S':
        shoot(command)
    else:
        move(command)



def move(command):
    global c_direction, c_x, c_y, board, change_direction, steps

    # 방향 바꾸기
    c_direction = change_direction[command]
    board[c_x][c_y] = direction_list[c_direction]

    nx, ny = c_x + steps[c_direction][0], c_y + steps[c_direction][1]
    # 평지이면 이동
    if nx < 0 or nx >= H or ny < 0 or ny >= W:
        return
    if board[nx][ny] == '.':
        board[c_x][c_y], board[nx][ny] = board[nx][ny], board[c_x][c_y]
        c_x, c_y = nx, ny



def shoot(command):
    global c_direction, c_x, c_y, board, steps

    # 발포
    i = 0
    while True:
        i += 1
        nx, ny = c_x + steps[c_direction][0]*i, c_y + steps[c_direction][1]*i
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            return
        # 벽돌 충돌
        if board[nx][ny] == '*':
            board[nx][ny] = '.'
            return
        elif board[nx][ny] == '#':
            return


T = int(input())
for TC in range(T):
    H, W = map(int, input().split())

    board = [list(input()) for _ in range(H)]

    N = int(input())
    user_commands = input()

    # 0: ^, 1: v, 2: <, 3: >
    direction_dict = {'^': 0, 'v': 1, '<': 2, '>': 3}
    direction_list = ['^', 'v', '<', '>']
    change_direction = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    steps = ((-1, 0), (+1, 0), (0, -1), (0, +1))

    # 현재 바라보는 방향 정하기
    # 현재 위치 찾기
    c_x, c_y = find_current()

    for command in user_commands:
        game(command)



    # 출력
    print(f'#{TC+1} ', end="")
    for i in range(H):
        for j in range(W):
            print(board[i][j], end="")
        print()