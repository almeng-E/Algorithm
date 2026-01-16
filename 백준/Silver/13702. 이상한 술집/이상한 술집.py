import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

L = 1
R = arr[-1]

ans = 0
while L <= R:
    cnt = 0
    mid = (L+R)//2
    for e in arr:
        cnt += e//mid
    if cnt < K:
        R = mid - 1
    else:
        L = mid + 1
        ans = mid

print(ans)