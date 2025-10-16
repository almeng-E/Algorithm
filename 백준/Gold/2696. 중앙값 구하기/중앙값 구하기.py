import sys
input = sys.stdin.readline

from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    res = []
    left = []   # max heap
    right = []  # min heap
    M = int(input())
    arr = []
    for i in range(0, M, 10):
        arr.extend(list(map(int, input().split())))
    for i in range(M):
        x = arr[i]
        if right:
            r = heappop(right)
            r *= -1
            heappush(left, r)
        x *= -1
        heappush(left, x)
        while len(left) > len(right):
            l = heappop(left)
            l *= -1
            heappush(right, l)

        if not (i & 1):
            res.append(right[0])

    print(len(res))
    for i in range(0, len(res), 10):
        print(*res[i:i+10])