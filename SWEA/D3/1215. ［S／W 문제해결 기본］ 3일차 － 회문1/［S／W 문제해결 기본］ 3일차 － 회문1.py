
for TC in range(10):
    N = int(input())
    res = 0

    board = [list(input()) for _ in range(8)]
    for i in range(8):
        for j in range(8-N+1):
            for k in range(N//2):
                if board[i][j+k] != board[i][j+N-1-k]:
                    break
            else:
                res += 1
            for k in range(N//2):
                if board[j+k][i] != board[j+N-1-k][i]:
                    break
            else:
                res += 1

    print(f'#{TC+1} {res}')
