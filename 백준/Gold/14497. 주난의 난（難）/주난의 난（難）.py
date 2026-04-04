import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
board = [list(input().rstrip()) for _ in range(N)]
INF = float('inf')
v = [[INF for _ in range(M)] for _ in range(N)]
steps = ((0, 1), (1, 0), (0, -1), (-1, 0))

q = deque()
q.append((x1, y1, 0))
v[x1][y1] = 0
while q:
    x, y, d = q.popleft()
    if v[x][y] < d:
        continue
    if x == x2 and y == y2:
        print(d)
        break

    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if board[nx][ny] == '0' or board[nx][ny] == '*':
            if v[nx][ny] > d:
                v[nx][ny] = d
                q.appendleft((nx, ny, d))  
        else:
            if v[nx][ny] > d+1:
                v[nx][ny] = d+1
                q.append((nx, ny, d+1))  