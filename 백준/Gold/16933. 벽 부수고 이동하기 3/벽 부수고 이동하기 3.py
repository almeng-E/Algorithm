from collections import deque
INF = float('inf')
steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))
N, M, K = map(int, input().split())

board = [input() for _ in range(N)]

# [부신 횟수][x][y]
visited = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(K+1)]

queue = deque()
queue.append((0, 0, 0, True, 1))
visited[0][0][0] = 1

while queue:
    x, y, walls_changed, day, dist = queue.popleft()

    if (x, y) == (N-1, M-1):
        continue
    if not day:
        new_dist = dist + 1
        queue.append((x, y, walls_changed, True, new_dist))

    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        new_dist = dist + 1

        if board[nx][ny] == "1" and walls_changed < K:
            if day:
                if visited[walls_changed+1][nx][ny] > new_dist:
                    visited[walls_changed+1][nx][ny] = new_dist
                    queue.append((nx, ny, walls_changed+1, False, new_dist))
        elif board[nx][ny] == "0":
            if visited[walls_changed][nx][ny] > new_dist:
                visited[walls_changed][nx][ny] = new_dist
                queue.append((nx, ny, walls_changed, not day, new_dist))
res = INF
for w in range(K+1):
    res = min(res, visited[w][N-1][M-1])

print(res if res != INF else -1)