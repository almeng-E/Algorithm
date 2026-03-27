import sys
input = sys.stdin.readline
from collections import deque
def main():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    
    steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
    v = [[0] * M for _ in range(N)]
    leaf = []
    for i in range(N):
        for j in range(M):
            if not v[i][j] and board[i][j] == 'L':
                q = deque()
                q.append((i, j))
                v[i][j] = 1
                while q:
                    x, y = q.popleft()
                    is_leaf = True
                    for dx, dy in steps:
                        nx, ny = x+dx, y+dy
                        if nx < 0 or nx >= N or ny < 0 or ny >= M or v[nx][ny] or board[nx][ny] == 'W':
                            continue
                        is_leaf = False
                        v[nx][ny] = 1
                        q.append((nx, ny))
                    if is_leaf:
                        leaf.append((x, y))
    
    ans = 0
    for x, y in leaf:
        v = [[0] * M for _ in range(N)]
        q = deque()
        q.append((x, y, 0))
        v[x][y] = 1
        while q:
            x, y, d = q.popleft()
            ans = max(ans, d)
            for dx, dy in steps:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M or v[nx][ny] or board[nx][ny] == 'W':
                    continue
                v[nx][ny] = 1
                q.append((nx, ny, d+1))
    
    print(ans)
main()