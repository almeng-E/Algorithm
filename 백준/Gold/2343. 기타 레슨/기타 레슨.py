import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

l, r = max(arr), sum(arr)
while l <= r:
    mid = (l+r) // 2

    cnt = 1
    cur = 0
    for a in arr:
        if a+cur <= mid:
            cur += a
        else:
            cnt += 1
            cur = a
    if cnt <= M:
        r = mid - 1
    else:
        l = mid + 1
print(l)