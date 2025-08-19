import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

arr = list(map(int, input().split()))

LEN = 1
while LEN < N:
    LEN <<= 1
SIZE = LEN * 2

tree = [0] * SIZE

for i in range(N):
    tree[i+LEN] = arr[i]

for i in range(LEN-1, 0, -1):
    tree[i] = tree[i*2] + tree[i*2 + 1]

for _ in range(Q):
    x, y, a, b = map(int, input().split())

    # 어우 문제 더러워
    if x > y:
        x, y = y, x
        
    tmp = 0
    left = x + LEN - 1
    right = y + LEN - 1

    while left <= right:
        if left & 1:
            tmp += tree[left]
            left += 1

        if not (right & 1):
            tmp += tree[right]
            right -= 1

        left >>= 1
        right >>= 1

    print(tmp)

    idx = a + LEN - 1

    tree[idx] = b
    idx >>= 1
    while idx >= 1:
        tree[idx] = tree[idx*2] + tree[idx*2 + 1]
        idx >>= 1
