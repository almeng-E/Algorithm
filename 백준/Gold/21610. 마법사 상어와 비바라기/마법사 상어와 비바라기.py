import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    steps = ((0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
    diag = (2, 4, 6, 8)
    
    clouds = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]
    
    for _ in range(M):
        d, s = map(int, input().split())
        rained = set()
        while clouds:
            x, y = clouds.pop()
            dx, dy = steps[d]
            nx = (x+dx*s) % N
            ny = (y+dy*s) % N
            board[nx][ny] += 1
            rained.add((nx, ny))
    
        for x, y in rained:
            for d in diag:
                dx, dy = steps[d]
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if board[nx][ny] != 0:
                    board[x][y] += 1
    
        for x in range(N):
            for y in range(N):
                if board[x][y] >= 2 and (x, y) not in rained:
                    clouds.append((x, y))
                    board[x][y] -= 2
    
    print(sum(map(sum, board)))

solve()