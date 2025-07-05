import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
tmp = 0
res = 2*N

while True:
    if tmp < S:
        if right == N:      # 더 이상 확장 불가
            break
        tmp += arr[right]
        right += 1
    else:
        res = min(res, right - left)
        tmp -= arr[left]
        left += 1

print(res if res <= N else 0)