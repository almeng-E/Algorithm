from collections import deque

def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]
    r_graph = [[] for _ in range(n+1)]
    for a, b in results:
        graph[a].append(b)
        r_graph[b].append(a)
    
    def bfs(v, gr):
        # BFS
        queue = deque()
        queue.append(v)
        visited = [False] * (n+1)
        visited[v] = True
        while queue:
            x = queue.popleft()
            for nx in gr[x]:
                if not visited[nx]:
                    visited[nx] = True
                    queue.append(nx)
        return sum(visited)
    
    for i in range(1, n+1):
        tmp = 0
        tmp += bfs(i, graph)
        tmp += bfs(i, r_graph)
        if tmp == (n+1):
            answer += 1

    return answer