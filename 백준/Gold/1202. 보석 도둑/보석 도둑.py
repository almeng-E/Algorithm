import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

heapq.heapify(gems)
bags.sort()

res = 0

compare = []
for bag in bags:

    # 내 보석 후보들을 찾자
    while gems:
        tmp = heapq.heappop(gems)
        if tmp[0] <= bag:
            m, v = tmp
            tmp = (-v, m)
            # compare : v 최대 힙
            heapq.heappush(compare, tmp)
        else:
            heapq.heappush(gems, tmp)
            break

    # 후보들 안에서 확인
    if compare:
        v, m = heapq.heappop(compare)
        res += v * -1
    else:
        continue

print(res)