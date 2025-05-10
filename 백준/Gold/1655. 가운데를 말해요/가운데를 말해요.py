import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heappushpop

left = [100001]   # max heap
right = [100001]  # min heap
is_even = 0

for i in range(int(input())):
    if not is_even:
        heappush(left, -heappushpop(right, -heappushpop(left, -int(input()))))

    else:
        heappush(right, -heappushpop(left, -int(input())))

    print(-left[0])
    is_even ^= 1