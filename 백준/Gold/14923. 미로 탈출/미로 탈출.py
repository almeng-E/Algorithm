from collections import deque

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 0-index 변환
Hx -= 1
Hy -= 1
Ex -= 1
Ey -= 1

steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))

# [부순 벽의 개수][x][y]
visited = [[[float('inf') for _ in range(M)] for _ in range(N)] for _ in range(2)]

queue = deque()
queue.append((Hx, Hy, 0))
visited[0][Hx][Hy] = 0

while queue:
    x, y, broken_wall = queue.popleft()

    if (x, y) == (Ex, Ey):
        break

    c_cost = visited[broken_wall][x][y]
    for dx, dy in steps:
        nx, ny = x+dx, y+dy

        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0:
                if visited[broken_wall][nx][ny] > c_cost + 1:
                    visited[broken_wall][nx][ny] = c_cost + 1
                    queue.append((nx, ny, broken_wall))
            else:
                if broken_wall == 0:
                    if visited[1][nx][ny] > c_cost + 1:
                        visited[1][nx][ny] = c_cost + 1
                        queue.append((nx, ny, 1))


res = min(visited[0][Ex][Ey], visited[1][Ex][Ey])
print(-1 if res == float('inf') else res)