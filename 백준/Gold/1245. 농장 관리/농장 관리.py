import sys
input = sys.stdin.readline
from collections import deque


def search(r, c):
    h = board[r][c]
    q = deque()
    q.append((r, c))
    v[r][c] = 1
    is_peak = True
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if board[nx][ny] > h:
                is_peak = False
            if not v[nx][ny] and board[nx][ny] == h:
                v[nx][ny] = 1
                q.append((nx, ny))
    return is_peak


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]

delta = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
ans = 0

for r in range(N):
    for c in range(M):
        if not v[r][c]:
            ans += search(r, c)
print(ans)