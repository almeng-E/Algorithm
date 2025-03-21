from heapq import heappop, heappush


def djikstra(s):
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

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y, c = map(int, input().split())
    graph[x].append((y, c))  # 다음 노드 , 가중치

res = 0
base_to_homes = djikstra(X)

for i in range(1, N + 1):
    if i != X:
        tmp = djikstra(i)
        res = max(res, tmp[X] + base_to_homes[i])

print(res)