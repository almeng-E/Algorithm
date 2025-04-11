
from collections import deque


def find_start(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                sx, sy = i, j
            elif board[i][j] == 'Y':
                ex, ey = i, j

    return sx, sy, ex, ey

#           상       우       하       좌
steps = ((-1, 0), (0, +1), (+1, 0), (0, -1))
INF = float('inf')
T = int(input())
for TC in range(T):
    N, K = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    sx, sy, ex, ey = find_start(N)

    queue = deque()
    queue.append((sx, sy, 0, 0))

    # [자른 나무 개수] [방향] [x] [y]
    visited = [[[[INF for _ in range(N)] for _ in range(N)] for _ in range(4)] for _ in range(K+1)]
    visited[0][0][sx][sy] = 0

    while queue:
        x, y, di, trees_removed = queue.popleft()
        current_cost = visited[trees_removed][di][x][y]

        # 도착지에 도달한 상태는 더 이상 확장하지 않음.
        if board[x][y] == 'Y':
            continue

        # 1. 전진 동작: 현재 방향(di)으로 한 칸 이동 (비용 +1)
        nx, ny = x + steps[di][0], y + steps[di][1]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == 'T':
                # 만약 나무 칸인데 제거 횟수를 남겼다면, 나무 제거하고 전진
                if trees_removed < K and current_cost + 1 < visited[trees_removed + 1][di][nx][ny]:
                    visited[trees_removed + 1][di][nx][ny] = current_cost + 1
                    queue.append((nx, ny, di, trees_removed + 1))
            else:
                # 땅('G') 또는 도착지('Y')이면 그냥 전진
                if current_cost + 1 < visited[trees_removed][di][nx][ny]:
                    visited[trees_removed][di][nx][ny] = current_cost + 1
                    queue.append((nx, ny, di, trees_removed))

        # 2. 회전 동작: 제자리에서 좌측 90도 회전 (비용 +1)
        nd = (di - 1) % 4
        if current_cost + 1 < visited[trees_removed][nd][x][y]:
            visited[trees_removed][nd][x][y] = current_cost + 1
            queue.append((x, y, nd, trees_removed))

        # 3. 회전 동작: 제자리에서 우측 90도 회전 (비용 +1)
        nd = (di + 1) % 4
        if current_cost + 1 < visited[trees_removed][nd][x][y]:
            visited[trees_removed][nd][x][y] = current_cost + 1
            queue.append((x, y, nd, trees_removed))

    res = INF
    for i in range(4):
        for j in range(0, K+1):
            res = min(res, visited[j][i][ex][ey])
    if res == INF:
        res = -1


    print(f'#{TC + 1} {res}')
