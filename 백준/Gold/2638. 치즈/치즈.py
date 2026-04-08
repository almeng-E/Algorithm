import sys
input = sys.stdin.readline
from collections import deque

def sol():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cheese = sum(map(sum, board))
    ans = 0
    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
    while cheese:
        ans += 1
        v = [[0] * M for _ in range(N)]
        q = deque()
        q.append((0, 0))
        v[0][0] = 2
        while q:
            x, y = q.popleft()
            for dx, dy in delta:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M or v[nx][ny] >= 2:
                    continue
                if board[nx][ny] == 0:
                    v[nx][ny] = 2
                    q.append((nx, ny))
                else:
                    v[nx][ny] += 1
                    if v[nx][ny] == 2:
                        board[nx][ny] = 0
                        cheese -= 1
    print(ans)
    
sol()