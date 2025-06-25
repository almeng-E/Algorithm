import sys
input = sys.stdin.readline

import heapq, bisect

N = int(input())
LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN << 1

tree = [[] for _ in range(SIZE)]
arr = list(map(int, input().split()))

for i in range(N):
    tree[i+LEN].append(arr[i])

for i in range(LEN-1, 0, -1):
    tree[i] = list(heapq.merge(tree[i<<1], tree[(i<<1) + 1]))


Q = int(input())
for _ in range(Q):
    i, j, k = map(int, input().split())

    cnt = 0

    left = LEN + i - 1
    right = LEN + j - 1

    while left <= right:
        if left & 1:
            cnt += len(tree[left]) - bisect.bisect_right(tree[left], k)
            left += 1

        if not right & 1:
            cnt += len(tree[right]) - bisect.bisect_right(tree[right], k)
            right -= 1

        left >>= 1
        right >>= 1

    print(cnt)