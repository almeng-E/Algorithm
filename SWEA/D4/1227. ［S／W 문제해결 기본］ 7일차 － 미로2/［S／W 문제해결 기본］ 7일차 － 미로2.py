from collections import deque


def bfs():
    sx, sy = find_start()

    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 100 and 0 <= ny < 100): continue
            if board[nx][ny] == 1: continue
            if board[nx][ny] == 3:
                return True
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return False

def find_start():
    for i in range(100):
        for j in range(100):
            if board[i][j] == 2:
                return i, j



steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))

for _ in range(10):
    TC = int(input())
    board = [list(map(int, input())) for _ in range(100)]

    visited = [[False for _ in range(100)] for _ in range(100)]

    flag = bfs()
    print(f'#{TC}', 1 if flag else 0)
