N = int(input())
k = int(input())

left = 1
right = N**2
res = 0

while left <= right:
    mid = (left + right) // 2

    idx_cnt = 0

    for i in range(1, N+1):
        idx_cnt += min(N, mid // i)

    if idx_cnt >= k:
        right = mid - 1
        res = mid
    else:
        left = mid + 1
print(res)