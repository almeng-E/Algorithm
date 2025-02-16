from collections import defaultdict, deque


T = 10
for TC in range(T):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))

    graph = defaultdict(list)
    # 진입 차수
    in_degree = defaultdict(int)

    # 그래프 저장
    for i in range(0, 2*E, 2):
        graph[edges[i]].append(edges[i+1])
        in_degree[edges[i+1]] += 1

    result = []

    # queue 풀이
    queue = deque()
    for i in range(1, V+1):
        if in_degree[i] == 0:
            queue.append(i)
    # queue 탐색
    while queue:
        node = queue.popleft()
        result.append(node)

        for next_node in graph[node]:
            in_degree[next_node] -= 1
            
            if in_degree[next_node] == 0:
                queue.append(next_node)

    print(f'#{TC+1}', *result)