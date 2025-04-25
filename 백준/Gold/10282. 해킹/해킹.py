import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(D):
        a, b, s = map(int, input().split())
        graph[b].append((a, s)) # b -> a (s)

    queue = deque()
    queue.append(C)
    time = [float('inf')] * (N+1)
    time[C] = 0

    while queue:
        x = queue.popleft()

        for nx, weight in graph[x]:
            if time[nx] > time[x] + weight:
                time[nx] = time[x] + weight
                queue.append(nx)

    v_cnt = 0
    t_max = 0


    for i in range(1, N+1):
        if time[i] != float('inf'):
            v_cnt += 1
            t_max = max(t_max, time[i])
    print(v_cnt, t_max)