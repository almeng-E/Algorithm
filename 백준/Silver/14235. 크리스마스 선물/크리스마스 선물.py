import heapq

N = int(input())
bag = []
for _ in range(N):
    a, *b = map(int, input().split())
    if a != 0:
        for i in b:
            heapq.heappush(bag, -i)
    else:
        if bag:
            print(-heapq.heappop(bag))
        else:
            print(-1)