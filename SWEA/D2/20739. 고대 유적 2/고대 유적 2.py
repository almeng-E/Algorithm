
# 체크
def check(i, j, dx, dy, board, N, M):
    sx = i
    sy = j


    # 정방향 체크
    cnt = 1
    while True:
        if 0 <= i+dx < N and 0 <= j+dy < M and board[i+dx][j+dy] == 1:
            i, j = i+dx, j+dy
            cnt += 1
        else:
            break
    if cnt == 1:
        return 0

    # 역방향 체크, 제외
    if 0 <= sx-dx < N and 0 <= sy-dy < M:
        if board[sx-dx][sy-dy] == 1:
            return 0
        else:
            return cnt
    else:
        return cnt

#        가로      세로
steps = ((0, +1), (+1, 0))

T = int(input())
for TC in range(T):
    res = 0
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                for dx, dy in steps:
                    tmp = check(i, j, dx, dy, board, N, M)
                    if res < tmp:
                        res = tmp
    if res > 0:
        print(f'#{TC+1} {res}')
    else:
        print(f'#{TC + 1} 0')


