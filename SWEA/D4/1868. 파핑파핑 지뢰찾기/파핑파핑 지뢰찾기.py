from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    near_bomb_count[x][y] = -1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy
            if 0 > nx or nx >= N or 0 > ny or ny >= N: continue;
            if near_bomb_count[nx][ny] == -1: continue;
            if near_bomb_count[nx][ny] == 0:
                queue.append((nx, ny))
            near_bomb_count[nx][ny] = -1


delta = ((0, +1), (0, -1), (+1, 0), (-1, 0), (+1, +1), (+1, -1), (-1, +1), (-1, -1))

T = int(input())
for TC in range(T):

    N = int(input())

    board = [list(input()) for _ in range(N)]
    near_bomb_count = [[0 for _ in range(N)] for _ in range(N)]

    # . 처리하기
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                near_bomb_count[i][j] = -1
            else:
                for dx, dy in delta:
                    nx, ny = i + dx, j + dy
                    if 0 > nx or nx >= N or 0 > ny or ny >= N: continue;
                    if board[nx][ny] == '*':
                        near_bomb_count[i][j] += 1
    # BFS , 클릭 개수 처리
    res = 0

    for i in range(N):
        for j in range(N):
            if near_bomb_count[i][j] == 0:
                bfs(i, j)
                res += 1


    for i in range(N):
        for j in range(N):
            if near_bomb_count[i][j] != -1:
                res += 1

    print(f'#{TC+1} {res}')
