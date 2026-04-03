from collections import deque

def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    INF = float('inf')
    steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
    
    
    q = deque()
    q.append((0, 0, 1))
    v = [[INF] * M for _ in range(N)]
    v[0][0] = 1
    while q:
        x, y, d = q.popleft()
        if x == N-1 and y == M-1:
            return d
        
        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M or maps[nx][ny] == 0:
                continue
            if v[nx][ny] > d+1:
                v[nx][ny] = d+1
                q.append((nx, ny, d+1))
    return -1               
