import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    board = [['.' for _ in range(M+2)]]
    for _ in range(N):
        board.append(['.'] + list(input().rstrip()) + ['.'])
    board.append(['.' for _ in range(M+2)])

    k = input().rstrip()
    keys = set()
    if k != '0':
        for c in k:
            keys.add(chr(ord(c)-32))
    v = [[0 for _ in range(M+2)] for _ in range(N+2)]
    ret = 0

    q = deque()
    q.append((0, 0))
    STEPS = ((0, 1), (0, -1), (1, 0), (-1, 0))
    door_q = dict()

    while q:
        x, y = q.popleft()
        for dx, dy in STEPS:
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=N+2 or ny<0 or ny>=M+2:
                continue
            if v[nx][ny]:
                continue
            if board[nx][ny] == '*':
                continue
            elif board[nx][ny] == '.':
                q.append((nx, ny))
                v[nx][ny] = 1
            elif board[nx][ny] == '$':
                ret += 1
                v[nx][ny] = 1
                q.append((nx, ny))
            else:
                if board[nx][ny] in keys:
                    q.append((nx, ny))
                    v[nx][ny] = 1
                elif 97 <= ord(board[nx][ny]) <= 122:
                    k = chr(ord(board[nx][ny]) - 32)
                    keys.add(k)
                    q.append((nx, ny))
                    v[nx][ny] = 1
                    if k in door_q:
                        for i, j in door_q[k]:
                            q.append((i, j))
                            v[i][j] = 1
                        del door_q[k]
                else:
                    if board[nx][ny] not in door_q:
                        door_q[board[nx][ny]] = []
                    door_q[board[nx][ny]].append((nx, ny))

    print(ret)