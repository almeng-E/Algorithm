from collections import deque

def solution(n, computers):
    answer = 0
    # 0 ~ n-1
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j]:
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue 
        answer += 1
        queue = deque()
        queue.append(i)
        visited[i] = True
        while queue:
            x = queue.popleft()
            for nx in graph[x]:
                if not visited[nx]:
                    visited[nx] = True
                    queue.append(nx)
           
    return answer