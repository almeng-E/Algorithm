import sys
input = sys.stdin.readline

def install(max_dist):
    cnt = 1
    last = home[0]

    for i in range(1, N):
        if home[i] - last >= max_dist:
            cnt += 1
            last = home[i]
    return cnt


N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()

l, r = 0, home[-1] - home[0] + 1
ans = 0
while l <= r:
    mid = (l+r) >> 1
    if install(mid) < C:
        r = mid - 1
    else:
        l = mid + 1
        ans = mid
print(ans)
