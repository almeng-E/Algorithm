from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    board = [list(input()) for _ in range(N)]

    res = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == '#':
                res += 1
                board[i][j] = 'X'
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()

                    for dx, dy in ((0, -1), (0, +1), (-1, 0), (+1, 0)):
                        nx, ny = x+dx, y+dy
                        if nx<0 or nx>=N or ny<0 or ny>=M: continue
                        if board[nx][ny] == '#':
                            q.append((nx, ny))
                            board[nx][ny] = 'X'
    print(res)