import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [[0 for _ in range(N)] for _ in range(N)]
M = N-K+1

pic = [[0 for _ in range(M)] for _ in range(M)]

ans = []

cur_max = 0
Q = int(input())
for _ in range(Q):
    r, c, v = map(int, input().split())
    r -= 1
    c -= 1

    diff = v - board[r][c]
    board[r][c] = v
    for i in range(max(0, r-K+1), min(r+1, M)):
        for j in range(max(0, c-K+1), min(c+1, M)):
            pic[i][j] += diff
            if cur_max < pic[i][j]:
                cur_max = pic[i][j]
    ans.append(cur_max)
print('\n'.join(map(str, ans)))