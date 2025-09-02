import sys
input = sys.stdin.readline
from heapq import heappop, heappush


house = []
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    house.append((a, b))

d = int(input())

house = [h for h in house if h[1] - h[0] <= d]
house.sort(key=lambda x: x[1])

res = 0
st = []
for s, e in house:
    while st and st[0][0] < e-d:
        heappop(st)
    heappush(st, (s, e))
    res = max(res, len(st))
print(res)

