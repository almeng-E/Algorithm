import sys
input = sys.stdin.readline

N, M = map(int, input().split())

LEN = 1
while LEN < N:
    LEN *= 2
SIZE = LEN * 2

# 트리 생성
tree = [(float('inf'), -float('inf')) for _ in range(SIZE)]  # (최솟값, 최댓값)

# 트리 채우기 - 1 : leaf 채우기
for i in range(N):
    a = int(input())
    tree[i+LEN] = (a, a)

# 트리 채우기
for i in range(LEN-1, 0, -1):
    mn = min(tree[i*2][0], tree[i*2 + 1][0])
    mx = max(tree[i*2][1], tree[i*2 + 1][1])
    tree[i] = (mn, mx)

# 쿼리 처리하기 (투포인터 탐색)
for _ in range(M):
    tmp_min = float('inf')
    tmp_max = -float('inf')

    left, right = map(int, input().split())
    left = left - 1 + LEN   # 0-index
    right = right - 1 + LEN  # 0-index

    while left <= right:
        if left % 2 == 1:
            tmp_min = min(tmp_min, tree[left][0])
            tmp_max = max(tmp_max, tree[left][1])
            left += 1
        if right % 2 == 0:
            tmp_min = min(tmp_min, tree[right][0])
            tmp_max = max(tmp_max, tree[right][1])
            right -= 1

        left //= 2
        right //= 2
    print(tmp_min, tmp_max)