import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

res = float('inf')
for i in range(N-1):
    left = i
    right = N-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] - arr[i] < M:
            left = mid + 1
        else:
            res = min(res, arr[mid] - arr[i])
            right = mid - 1

print(res)