import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T):
    K, M, P = map(int, input().split())

    graph = [[] for _ in range(M+1)]
    in_degree = [0 for _ in range(M+1)]

    for _ in range(P):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1

    visited = [-1 for _ in range(M + 1)]
    max_counted = [0 for _ in range(M+1)]


    queue = deque()
    for i in range(1, M):
        if in_degree[i] == 0:
            queue.append(i)
            visited[i] = 1

    while queue:
        x = queue.popleft()

        # 갱신 logic
        for nx in graph[x]:
            in_degree[nx] -= 1

            if visited[nx] == -1:       # 첫 방문
                visited[nx] = visited[x]
                max_counted[nx] = 1
            else:
                if visited[nx] == visited[x]:   # 값이 같네?
                    max_counted[nx] += 1
                    if max_counted[nx] == 2:    # 두개 이상 받음
                        visited[nx] += 1
                        max_counted[nx] = 0
                elif visited[nx] < visited[x]:
                    visited[nx] = visited[x]
                    max_counted[nx] = 1

        # enqueue 로직
            if in_degree[nx] == 0:
                queue.append(nx)

    print(K, visited[M])