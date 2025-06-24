N = int(input())
r = [int(input()) for _ in range(N)]
r.sort()
res = 0
for i in range(N):
    res = max(res, r[i], r[i]*(N-i))
print(res)
