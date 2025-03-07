import sys
input=sys.stdin.readline
def dfs(x, y):
    global group

    visited[x][y] = -1 # 임시 경로

    dx, dy = steps[flute[board[x][y]]]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < M:
        if visited[nx][ny] == 0:
            g_num = dfs(nx, ny)
        # 다음 칸이 이미 방문한 값임
        else:
            # 이번 회차에 방문한 값이면
            if visited[nx][ny] == -1:
                g_num = group
            # 지난 회차에 방문한 값이면
            else:
                g_num = visited[nx][ny]
    # 다음 칸이 out of index
    else:
        g_num = group
    visited[x][y] = g_num
    return g_num


N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

flute = {
    'D': 0,
    'U': 1,
    'R': 2,
    'L': 3,
}

visited = [[0 for _ in range(M)] for _ in range(N)]
steps = ((+1, 0), (-1, 0), (0, +1), (0, -1))
group = 1
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            tmp = dfs(i, j)
            if tmp == group:
                group += 1

print(group-1)