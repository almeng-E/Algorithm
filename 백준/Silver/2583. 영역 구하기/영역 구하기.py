import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global tmp
    tmp += 1
    visited[x][y] = True

    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < N and 0 <= ny < M): continue
        if not board[nx][ny]: continue
        if visited[nx][ny]: continue
        dfs(nx, ny)



steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))

# N*M 사이즈
M, N, K = map(int, input().split())

board = [[True for _ in range(M)] for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            board[i][j] = False

area = []

for i in range(N):
    for j in range(M):
        if board[i][j] and not visited[i][j]:
            tmp = 0
            dfs(i, j)
            area.append(tmp)

print(len(area))
print(*sorted(area))