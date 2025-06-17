import sys
input = sys.stdin.readline

from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))
res = []

queue = deque()
# queue.append((0, -float('inf')))

for i, v in enumerate(arr):
    if i-L >= 0 and queue[0][0] <= i-L:
        queue.popleft()

    if not queue:
        queue.append((i, v))
    else:
        while queue and queue[-1][1] >= v:
            queue.pop()
        queue.append((i, v))


    res.append(str(queue[0][1]))

print(" ".join(res))

