import sys
input = sys.stdin.readline


N = int(input())

arr = [0] + [int(input()) for _ in range(N)]

dp_one = [0] * (N+1)
dp_two = [0] * (N+1)

dp_one[1] = arr[1]
dp_two[1] = arr[1]

for i in range(2, N+1):
    dp_one[i] = dp_two[i-1] + arr[i]
    dp_two[i] = max(dp_one[i-2] + arr[i], dp_two[i-2] + arr[i])

print(max(dp_one[N], dp_two[N]))