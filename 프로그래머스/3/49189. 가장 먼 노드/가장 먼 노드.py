from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    depth = [-1] * (n+1)  
    queue = deque()
    queue.append(1)
    depth[1] = 0
    
    while True:
        next_queue = deque()
        for x in queue:
            for nx in graph[x]:
                if depth[nx] == -1:
                    depth[nx] = depth[x] + 1
                    next_queue.append(nx)
        print(next_queue)
        if next_queue:
            answer = len(next_queue)
            queue = next_queue
        else:
            break
       
    return answer