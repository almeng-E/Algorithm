import sys
input = sys.stdin.readline

from heapq import heappop, heappush

L = []  # max
R = []  # min
cur = 0
ans = 0

N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == '1':
        x = int(cmd[1])
        if x <= cur:
            heappush(L, -x)
        else:
            heappush(R, x)
    else:
        while L or R:
            if L and R:
                ll = heappop(L)
                ll *= -1
                rr = heappop(R)

                if abs(cur-ll) <= abs(rr-cur):
                    ans += abs(cur-ll)
                    cur = ll
                    heappush(R, rr)
                else:
                    ans += abs(rr-cur)
                    cur = rr
                    heappush(L, -ll)
            elif L and not R:
                ll = heappop(L)
                ll *= -1
                ans += abs(cur-ll)
                cur = ll
            elif R and not L:
                rr = heappop(R)
                ans += abs(rr-cur)
                cur = rr
            else:
                pass
print(ans)