import sys
input = sys.stdin.readline

import heapq

N = int(input())
hq = []

for _ in range(N):
    hq.append(int(input()))

heapq.heapify(hq)
res = 0
while len(hq) > 1:
    tmp = heapq.heappop(hq) + heapq.heappop(hq)
    res += tmp
    heapq.heappush(hq, tmp)
print(res)