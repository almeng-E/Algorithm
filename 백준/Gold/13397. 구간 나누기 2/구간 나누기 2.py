import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))

lo = 0
hi = max(arr)-min(arr)
ans = 0

while lo <= hi:
    mid = (lo+hi) >> 1

    cnt = 1
    cur_min = arr[0]
    cur_max = arr[0]
    for i in range(1, N):
        cur_min = min(cur_min, arr[i])
        cur_max = max(cur_max, arr[i])
        if cur_max - cur_min > mid:
            cnt += 1
            cur_min = arr[i]
            cur_max = arr[i]

    if cnt <= M:
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans)