from collections import deque
def solution(maps):
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
    
    N = len(maps)
    M = len(maps[0])
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (N-1, M-1):
            break
        
        for dx, dy in steps:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    return visited[N-1][M-1]