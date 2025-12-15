import sys
input = sys.stdin.readline
from collections import deque

# 문제를 잘읽읍시다...

steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]
T = int(input())
for _ in range(T):
    H, W, O, F, Sx, Sy, Ex, Ey = map(int, input().split())
    board = [[0 for _ in range(W)] for _ in range(H)]
    for _ in range(O):
        x, y, l = map(int, input().split())
        board[x-1][y-1] = l
    Sx -= 1
    Sy -= 1
    Ex -= 1
    Ey -= 1
    q = deque()
    q.append((Sx, Sy))
    v = [[-1 for _ in range(W)] for _ in range(H)]
    v[Sx][Sy] = F
    while q:
        x, y = q.popleft()
        if x == Ex and y == Ey:
            print('잘했어!!')
            break
        if v[x][y] <= 0:
            continue
        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if board[nx][ny] <= board[x][y]:
                if v[nx][ny] < v[x][y] - 1:
                    v[nx][ny] = v[x][y] - 1
                    q.append((nx, ny))
            else:
                if v[x][y] >= board[nx][ny] - board[x][y]:
                    if v[nx][ny] < v[x][y] - 1:
                        v[nx][ny] = v[x][y] - 1
                        q.append((nx, ny))
    else:
        print('인성 문제있어??')