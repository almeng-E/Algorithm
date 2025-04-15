import sys
input = sys.stdin.readline

import heapq

N = int(input())

# 날짜 최대 힙
hq = []
max_day = 0
for _ in range(N):
    # p(강연료) , d(기한)
    p, d = map(int, input().split())
    heapq.heappush(hq, (-d, p))
    max_day = max(max_day, d)


res = 0
# 가격 최대 힙
tmp_li = []

for day in range(max_day+1, 0, -1):
    while hq:
        tmp = heapq.heappop(hq)
        d, p = tmp
        if -d >= day:
            heapq.heappush(tmp_li, -p)
        else:
            heapq.heappush(hq, tmp)
            break

    if tmp_li:
        tmp = heapq.heappop(tmp_li)
        res += -tmp
print(res)