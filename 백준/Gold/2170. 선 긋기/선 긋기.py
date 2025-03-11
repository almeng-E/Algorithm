import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    li.append((a, b))

li.sort(key=lambda x: (x[0], x[1]))

res = 0


ml, mr = li[0]
res += (mr - ml)
for i in range(1, N):
    tl, tr = li[i]
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