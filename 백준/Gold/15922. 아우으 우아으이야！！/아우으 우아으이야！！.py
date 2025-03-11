import sys
input = sys.stdin.readline

N = int(input())

res = 0
ml, mr = map(int, input().split())
res += (mr - ml)
for _ in range(N-1):
    tl, tr = map(int, input().split())

    if tr <= mr:
        continue
    if tl <= mr:
        res += tr - mr
        mr = tr
        continue
    if mr <= tl:
        res += tr - tl
        ml, mr = tl, tr
        continue


print(res)
