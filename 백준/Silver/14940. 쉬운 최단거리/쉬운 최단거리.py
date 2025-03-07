import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            x, y = i, j
        if board[i][j] == 0:
            visited[i][j] = 0


queue = deque()
queue.append((x, y))
visited[x][y] = 0

while queue:
    cx, cy = queue.popleft()

    for dx, dy in ((+1, 0), (-1, 0), (0, +1), (0, -1)):
        nx, ny = cx + dx, cy + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if board[nx][ny] == 0: continue
        if visited[nx][ny] == -1:
            visited[nx][ny] = visited[cx][cy]+1
            queue.append((nx, ny))


for row in visited:
    print(*row)