import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

DP = [[-1 for _ in range(M)] for _ in range(N)]


def dfs(x, y):
    # 이미 방문
    if DP[x][y] >= 0:
        return DP[x][y]

    # 첫 방문 -> DFS
    tmp = 0

    if (x, y) == (N-1, M-1):
        tmp += 1

    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] < board[x][y]:
            tmp += dfs(nx, ny)

    DP[x][y] = tmp
    return DP[x][y]


res = dfs(0, 0)
print(res)




