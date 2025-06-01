import sys
input = sys.stdin.readline

# 세그먼트 트리 생성하기
N, M, K = map(int, input().split())
LEN = 1
while LEN < N:
    LEN <<= 1     # = LEN *= 2
SIZE = 2 * LEN
tree = [0] * SIZE

# make-tree
for i in range(N):
    tree[i+LEN] = int(input())

# set-tree
for i in range(LEN-1, 0, -1):
    tree[i] = tree[i*2] + tree[i*2 + 1]

# 쿼리 단계
for _ in range(M+K):
    cmd = list(map(int, input().split()))

    # 변경
    if cmd[0] == 1:
        idx = cmd[1] - 1 + LEN
        tree[idx] = cmd[2]
        idx //= 2
        while idx >= 1:
            tree[idx] = tree[idx*2] + tree[idx*2 + 1]
            idx //= 2

    # 구간 합 쿼리
    elif cmd[0] == 2:
        left = cmd[1] - 1 + LEN
        right = cmd[2] - 1 + LEN

        s = 0
        while left <= right:
            if left % 2 == 1:
                s += tree[left]
                left += 1
            if right % 2 == 0:
                s += tree[right]
                right -= 1
            left //= 2
            right //= 2
        print(s)