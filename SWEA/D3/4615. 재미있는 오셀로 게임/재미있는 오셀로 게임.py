def game(x, y, my_stone):
    # 돌 구분
    if my_stone == 1:
        op_stone = 2
    else:
        op_stone = 1

    # 돌 놓기
    board[x][y] = my_stone

    # 팔방 탐색
    for dx, dy in steps:
        i = 0
        # 끝까지 가며 길의 끝에 내 돌이 하나라도 있는지 체크
        changing = False
        while True:
            i += 1
            nx, ny = x + dx*i, y + dy*i
            if not (0 <= nx < N and 0 <= ny < N): break

            if board[nx][ny] == 0:
                changing = False
                break
            elif board[nx][ny] == op_stone:
                continue
            elif board[nx][ny] == my_stone:
                changing = True
                break

        i = 0
        # 내 돌을 만날 때 까지 변환
        if changing:
            while True:
                i += 1
                nx, ny = x + dx*i, y + dy*i
                if not (0 <= nx < N and 0 <= ny < N): break
                # 변환 시작
                if board[nx][ny] == op_stone:
                    board[nx][ny] = my_stone
                elif board[nx][ny] == my_stone:
                    break


T = int(input())
steps = ((0, -1), (0, +1), (-1, 0), (+1, 0), (-1, -1), (-1, +1), (+1, -1), (+1, +1))
for TC in range(T):
    N, M = map(int, input().split())

    board = [[0 for _ in range(N)] for _ in range(N)]

    # 흑돌:1 백돌:2 초기 위치 처리
    board[N//2-1][N//2-1], board[N//2][N//2] = 2, 2
    board[N//2][N//2-1], board[N//2-1][N//2] = 1, 1

    for _ in range(M):
        x, y, stone = map(int, input().split())
        # 인덱스 보정하여 게임 진행
        game(x-1, y-1, stone)


        # for row in board:
        #     print(*row)
        # print('-' * 30)

    # 출력
    b_cnt = 0
    w_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] == 2:
                w_cnt += 1
    print(f'#{TC+1} {b_cnt} {w_cnt}')