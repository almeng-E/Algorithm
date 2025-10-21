import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

v = [[0 for _ in range(N)] for _ in range(N)]
steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
res = 0

def dfs(x, y):
    cnt = 1
    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[nx][ny] <= board[x][y]:
            continue

        if not v[nx][ny]:
            cnt = max(cnt, dfs(nx, ny) + 1)
            v[x][y] = cnt
        else:
            cnt = max(cnt, v[nx][ny] + 1)
            v[x][y] = cnt
    v[x][y] = cnt
    return cnt


for i in range(N):
    for j in range(N):
        if not v[i][j]:
            dfs(i, j)
            res = max(v[i][j], res)

print(res)