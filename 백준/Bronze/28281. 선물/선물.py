N, X = map(int, input().split())
arr = list(map(int, input().split()))
res = float('inf')
for i in range(N-1):
    res = min(res, X*(arr[i] + arr[i+1]))

print(res)