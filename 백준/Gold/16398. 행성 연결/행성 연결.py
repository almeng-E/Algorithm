import sys
input = sys.stdin.readline

from heapq import  heappop, heappush

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
used = [False] * N

MST = [1e10] * N
MST[0] = 0

hq = []
hq.append((0, 0))

while hq:
    c_dist, c_node = heappop(hq)

    if used[c_node] or c_dist > MST[c_node]: continue;

    used[c_node] = True

    for j in range(N):
        if not used[j] and costs[c_node][j] < MST[j]:
            MST[j] = costs[c_node][j]
            heappush(hq, (MST[j], j))


print(sum(MST))