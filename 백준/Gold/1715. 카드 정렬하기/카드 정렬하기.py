import heapq

N = int(input())
hq = []

for _ in range(N):
    heapq.heappush(hq, int(input()))
res = 0
while len(hq) > 1:
    tmp = heapq.heappop(hq) + heapq.heappop(hq)
    res += tmp
    heapq.heappush(hq, tmp)
print(res)