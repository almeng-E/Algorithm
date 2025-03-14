N, K = map(int, input().split())

arr = list(map(int, input().split()))

tmp_sum = sum(arr[:K])
res = tmp_sum


for i in range(K, N):
    tmp_sum -= arr[i-K]
    tmp_sum += arr[i]
    res = max(res, tmp_sum)

print(res)