from collections import deque


steps = ((0, +1), (+1, 0), (-1, 0), (0, -1))
T = int(input())
for TC in range(T):
    N = int(input())

    board = [list(map(int, input())) for _ in range(N)]
    visited = [[float('inf') for _ in range(N)] for _ in range(N)]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] > visited[x][y] + board[nx][ny]:
                    visited[nx][ny] = visited[x][y] + board[nx][ny]
                    queue.append((nx, ny))

    print(f'#{TC+1} {visited[N-1][N-1]}')