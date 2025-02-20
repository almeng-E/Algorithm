from collections import defaultdict, deque

for TC in range(10):
    L, START = map(int, input().split())

    # 그래프 (중복 가능)
    graph = defaultdict(set)
    # 빈 리스트 보다는 set
    visited = set()
    # { depth : [node1, node2, ... ] , ...}
    res_dict = defaultdict(list)

    edges = list(map(int, input().split()))
    # 그래프 저장
    for i in range(0, L, 2):
        graph[edges[i]].add(edges[i+1])

    # BFS 순회
    queue = deque()
    queue.append((START, 0))

    while queue:
        c_node, depth = queue.popleft()

        res_dict[depth].append(c_node)

        for next_node in graph[c_node]:
            if next_node not in visited:
                queue.append((next_node, depth+1))
                # 방문 처리
                visited.add(next_node)

    # 최대 깊이의 최댓값 찾기
    res = max(res_dict[max(res_dict.keys())])

    print(f'#{TC+1} {res}')