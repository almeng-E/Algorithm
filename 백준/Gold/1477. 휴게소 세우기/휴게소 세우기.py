import sys
input = sys.stdin.readline


N, M, L = map(int, input().split())
if N == 0:
    input()
    arr = [0, L]
else:
    arr = [0] + list(map(int, input().split())) + [L]
arr.sort()

# 휴게소가 없는 구간의 길이의 최댓값...의 최솟값
lo = 1
hi = L
ans = L
while lo <= hi:
    # 없는 구간의 최댓값
    mid = (lo+hi) >> 1
    cnt = 0
    for i in range(N+1):
        d = arr[i+1]-arr[i]
        cnt += (d-1) // mid

    if cnt <= M:
        ans = min(ans, mid)
        hi = mid-1
    else:
        lo = mid+1
print(ans)
