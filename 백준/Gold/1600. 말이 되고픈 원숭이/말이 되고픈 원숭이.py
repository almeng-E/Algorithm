from collections import deque

K = int(input())
M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

knight = [
    ( 2,  1),
    ( 2, -1),
    (-2,  1),
    (-2, -1),
    ( 1,  2),
    ( 1, -2),
    (-1,  2),
    (-1, -2),
]

steps = [(0, +1), (0, -1), (+1, 0), (-1, 0)]
visited = [[[float('inf') for _ in range(M)] for _ in range(N)] for _ in range(K+1)]
# 점프횟수 / x / y
visited[0][0][0] = 0
queue = deque()
queue.append((0, 0, 0))

while queue:
    x, y, jumped = queue.popleft()

    if (x, y) == (N - 1, M - 1):
        break

    cost = visited[jumped][x][y]
    if jumped < K:
        for dx, dy in knight:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 1:
                continue

            if visited[jumped+1][nx][ny] > cost + 1:
                visited[jumped+1][nx][ny] = cost + 1
                queue.append((nx, ny, jumped+1))

    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == 1:
            continue
        if visited[jumped][nx][ny] > cost + 1:
            visited[jumped][nx][ny] = cost + 1
            queue.append((nx, ny, jumped))

res = float('inf')
for i in range(K+1):
    res = min(res, visited[i][N-1][M-1])

print(res if res != float('inf') else -1)