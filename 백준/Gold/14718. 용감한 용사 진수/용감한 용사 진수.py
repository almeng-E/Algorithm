import sys
input = sys.stdin.readline
N, K = map(int, input().split())

STR = set()
DEX = set()
INT = set()

opp = []
for _ in range(N):
    a, b, c = map(int, input().split())
    opp.append((a, b, c))
    STR.add(a)
    DEX.add(b)
    INT.add(c)
#
# STR = sorted(STR)
# DEX = sorted(DEX)
# INT = sorted(INT)

res = float('inf')
for s in STR:
    for d in DEX:
        for i in INT:
            cnt = 0
            for o_s, o_d, o_i in opp:
                if o_s <= s and o_d <= d and o_i <= i:
                    cnt += 1
            if cnt >= K:
                res = min(res, s+d+i)
print(res)
