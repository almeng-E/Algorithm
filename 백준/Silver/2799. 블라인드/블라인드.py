import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().rstrip() for _ in range(5*N+1)]

ans = [0, 0, 0, 0, 0]

for i in range(N):
    for j in range(M):
        x = 1 + 5*i
        y = 1 + 5*j
        cnt = 0
        for k in range(4):
            if board[x+k][y:y+4] == '****':
                cnt += 1
            else:
                break
        ans[cnt] += 1
print(*ans)
