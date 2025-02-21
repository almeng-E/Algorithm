import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, color, dfs_table, visit_table):
    if color == 'B':
        visit_table[x][y] = 1
    else:
        visit_table[x][y] = 2

    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N): continue
        if not visit_table[nx][ny] and dfs_table[nx][ny] == color:
            dfs(nx, ny, color, dfs_table, visit_table)


steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))

N = int(input())

board = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

RGB_count = 0
RG_count = 0
B_count = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, board[i][j], board, visited)
            RGB_count += 1

new_visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if new_visited[i][j]: continue
        if not new_visited[i][j] and visited[i][j] == 2:
            dfs(i, j, 2, visited, new_visited)
            RG_count += 1
        else:
            dfs(i, j, 1, visited, new_visited)
            B_count += 1

print(RGB_count, RG_count+B_count)
