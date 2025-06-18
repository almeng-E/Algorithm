import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

res = float('inf')
j = 0
for i in range(N):
    while j < N and arr[j] - arr[i] < M:
        j += 1
    if j == N:
        break
    res = min(res, arr[j] - arr[i])

print(res)