import sys
input = sys.stdin.readline

import heapq


N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    # 유향
    graph[a].append((b, c))


# 거리 초기화
# K개의 오름차순 정렬된 거리정보
distance = [[float('inf') for _ in range(K)] for _ in range(N+1)]
distance[1][0] = 0

hq = []
heapq.heappush(hq, (0, 1))  # 현재까지의 거리, 노드

while hq:
    c_dist, c_node = heapq.heappop(hq)


    # 다음 노드 후보 넣기
    for n_node, weight in graph[c_node]:
        cost = c_dist + weight
        if distance[n_node][-1] > cost:
            distance[n_node].append(cost)
            distance[n_node].sort()
            distance[n_node].pop()
            heapq.heappush(hq, (cost, n_node))


for i in range(1, N+1):
    # distance[i] ... K번째 출력
    tmp = distance[i][-1]
    if tmp == float('inf'):
        print(-1)
    else:
        print(tmp)
