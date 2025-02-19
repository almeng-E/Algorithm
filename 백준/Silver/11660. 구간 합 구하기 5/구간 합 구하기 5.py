import sys
input = sys.stdin.readline


N, M = map(int, input().split())

board = [[0 for _ in range(N+1)]]
for _ in range(N):
    board.append([0] + list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        board[i][j] += board[i][j-1]

for _ in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())
    tmp = 0
    for i in range(X1, X2+1):
        tmp += board[i][Y2]
        tmp -= board[i][Y1-1]
    
    print(tmp)
