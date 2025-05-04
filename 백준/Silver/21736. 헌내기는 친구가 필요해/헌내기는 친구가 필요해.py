from collections import deque

N, K = map(int, input().split())

board = [list(input()) for _ in range(N)]

steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))

queue = deque()
for i in range(N):
    for j in range(K):
        if board[i][j] == 'I':
            queue.append((i, j))
            board[i][j] = 'X'
            break
    if queue:
        break

res = 0
while queue:
    x, y = queue.popleft()
    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= K:
            continue
        if board[nx][ny] == 'X':
            continue
        if board[nx][ny] == 'P':
            res += 1
        board[nx][ny] = 'X'
        queue.append((nx, ny))

print(res if res != 0 else 'TT')