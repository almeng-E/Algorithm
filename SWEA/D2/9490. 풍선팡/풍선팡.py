T = int(input())
for TC in range(T):
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    #       상       좌       하       우
    steps = ((-1, 0), (0, +1), (+1, 0), (0, -1))
    res = 0
    for i in range(N):
        for j in range(M):
            tmp = board[i][j]
            amount = board[i][j]
            for dx, dy in steps:
                for times in range(1, amount+1):
                    if 0 <= i + dx * times < N and 0 <= j + dy * times < M:
                        tmp += board[i + dx * times][j + dy * times]
            if res < tmp:
                res = tmp
    print(f'#{TC+1} {res}')