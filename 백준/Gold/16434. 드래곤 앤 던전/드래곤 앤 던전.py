import sys
input = sys.stdin.readline

N, H_ATK = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]


l = 1
r = int(9e18)
ans = int(9e18)
while l <= r:
    mid = (l+r) >> 1
    MAX_HP = mid
    CUR_HP = MAX_HP
    ATK = H_ATK

    for t, a, h in room:
        if t == 1:
            turns = h//ATK
            h %= ATK
            if h == 0:
                CUR_HP -= a*(turns-1)
            else:
                CUR_HP -= a*turns
            if CUR_HP <= 0:
                break
        else:
            ATK += a
            CUR_HP = min(CUR_HP+h, MAX_HP)
    else:
        ans = min(ans, mid)
        r = mid-1
        continue
    l = mid+1
print(ans)
