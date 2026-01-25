import sys
input = sys.stdin.readline

E, EM, M, MH, H = map(int, input().split())

total = E + EM + M + MH + H

ans = 0
s, e = 0, min(E+EM, MH+H)
while s <= e:
    mid = (s + e) // 2
    max_M = EM + M + MH

    if mid > E:
        max_M -= mid - E
    if mid > H:
        max_M -= mid - H

    if max_M >= mid:
        ans = mid
        s = mid+1
    else:
        e = mid-1

print(ans)
