import sys
input = sys.stdin.readline

from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

used = set()

steps = ((0, 1), (1, 0))

q = deque()
q.append((0, 0))
used.add((0, 0))

res = False
while q:
    x, y = q.popleft()

    if (x, y) == (N-1, M-1):
        res = True
        break

    for dx, dy in steps:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not board[nx][ny]:
            continue
        if (nx, ny) in used:
            continue
        q.append((nx, ny))
        used.add((nx, ny))


print('Yes' if res else 'No')