import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def solve():
    
    def find_pos(board):
        ret = []
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'C':
                    ret.append(i)
                    ret.append(j)
                    if len(ret) == 4:
                        return ret
    
    
    M, N = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    sx, sy, ex, ey = find_pos(board)
    INF = float('inf')
    step = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
    # curves, distance, direction, x, y
    hq = []
    # dist[direction][x][y] = curves
    dist = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(4)]
    for i in range(4):
        heappush(hq, (0, 0, i, sx, sy))
        dist[i][sx][sy] = 0
    
    while hq:
        curves, distance, direction, x, y = heappop(hq)
        if dist[direction][x][y] < curves:
            continue
        if (x, y) == (ex, ey):
            continue
    
        for n_direction in range(4):
            if n_direction == (direction+2) % 4:
                continue
            nx, ny = x + step[n_direction][0], y + step[n_direction][1]
            if nx>=N or nx<0 or ny>=M or ny<0 or board[nx][ny] == '*':
                continue
            n_curves = curves
            n_distance = distance + 1
            if n_direction != direction:
                n_curves += 1
    
            if dist[n_direction][nx][ny] > n_curves:
                dist[n_direction][nx][ny] = n_curves
                heappush(hq, (n_curves, n_distance, n_direction, nx, ny))
    
    ans = INF
    for i in range(4):
        ans = min(ans, dist[i][ex][ey])
    print(ans)
    
solve()