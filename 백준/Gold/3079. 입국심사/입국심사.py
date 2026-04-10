import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()

l = 1
r = 10**20
ans = r
while l <= r:
    mid = (l+r)//2
    cnt = 0
    for t in T:
        if t > mid:
            break
        cnt += mid//t
    if cnt >= M:
        ans = min(ans, mid)
        r = mid - 1
    else:
        l = mid + 1
print(ans)