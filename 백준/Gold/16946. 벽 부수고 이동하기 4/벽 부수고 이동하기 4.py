import sys
input = sys.stdin.readline
from collections import deque


steps = ((0, +1), (0, -1), (+1, 0), (-1, 0))
N, M = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(N)]

group = [[0 for _ in range(M)] for _ in range(N)]

size_memo = {}
id = 1
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and not group[i][j]:
            group[i][j] = id
            cnt = 0
            queue = deque()
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                cnt += 1
                for dx, dy in steps:
                    nx, ny = x+dx, y+dy
                    if 0<= nx < N and 0 <= ny < M and board[nx][ny] == 0 and not group[nx][ny]:
                        group[nx][ny] = id
                        queue.append((nx, ny))
            size_memo[id] = cnt%10
            id += 1




for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            used = set()
            for dx, dy in steps:
                nx, ny = i+dx, j+dy
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and group[nx][ny] not in used:
                    board[i][j] += size_memo[group[nx][ny]] % 10
                    used.add(group[nx][ny])
        print(board[i][j]%10, end="")
    print()