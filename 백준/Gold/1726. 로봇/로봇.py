from collections import deque

# 1-index :     1 동 2 서 3 남 4 북
steps = ((0,), (0, +1), (0, -1), (+1, 0), (-1, 0))

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
Sx, Sy, Sdi = map(int, input().split())
Sx -= 1
Sy -= 1
Gx, Gy, Gdi = map(int, input().split())
Gx -= 1
Gy -= 1

queue = deque()
queue.append((Sx, Sy, Sdi, 0))

# 3차원 visited 저장 [방향][x][y]
visited = [[[float('inf') for _ in range(M)] for _ in range(N)] for _ in range(5)]
visited[Sdi][Sx][Sy] = 0


while queue:
    x, y, di, cnt = queue.popleft()
    if x == Gx and y == Gy and di == Gdi:
        break

    for d in range(1, 5):
        if di == d:
            for i in range(1, 4):
                nx, ny = x + steps[d][0]*i, y + steps[d][1]*i
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                    break
                elif 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and visited[d][nx][ny] > cnt+1:
                    visited[d][nx][ny] = cnt + 1
                    queue.append((nx, ny, d, cnt + 1))
        else:
            if (di, d) in {(1, 2), (2, 1), (3, 4), (4, 3)}:
                if visited[d][x][y] > cnt + 2:
                    visited[d][x][y] = cnt + 2
                    queue.append((x, y, d, cnt + 2))
            else:
                if visited[d][x][y] > cnt + 1:
                    visited[d][x][y] = cnt + 1
                    queue.append((x, y, d, cnt + 1))

print(visited[Gdi][Gx][Gy])