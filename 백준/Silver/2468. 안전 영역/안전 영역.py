import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, limit):
    visited[x][y] = True

    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N): continue
        if not visited[nx][ny] and board[nx][ny] > limit:
            dfs(nx, ny, limit)





steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


# 최대, 최소 높이 찾기
max_height = max(max(row) for row in board)
min_height = min(min(row) for row in board)


res = 0

for h in range(min_height-1, max_height):
    # h 초과 들만 체크하도록 dfs
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > h:
                dfs(i, j, h)
                cnt += 1
    res = max(res, cnt)
print(res)