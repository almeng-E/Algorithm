from heapq import heappop, heappush

def djikstra(s, graph):
    global res
    distance = [INF] * (N + 1)

    hq = []
    heappush(hq, (0, s))
    distance[s] = 0

    while hq:
        c_dist, c_node = heappop(hq)

        if distance[c_node] < c_dist:
            continue

        for n_path in graph[c_node]:
            n_node, weight = n_path

            if distance[n_node] > c_dist + weight:
                distance[n_node] = c_dist + weight
                heappush(hq, (distance[n_node], n_node))

    return distance

INF = float('inf')
T = int(input())
for TC in range(T):
    N, M, X = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    r_graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))  # 다음 노드 , 가중치
        r_graph[y].append((x, c))

    res = 0
    party_to_home = djikstra(X, graph)
    home_to_party = djikstra(X, r_graph)

    for i in range(1, N + 1):
        if i != X:
            res = max(res, party_to_home[i] + home_to_party[i])

    print(f'#{TC+1} {res}')