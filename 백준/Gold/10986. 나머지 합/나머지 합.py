import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

cnt = [0] * (M+1)

acc = 0
for num in arr:
    acc += num
    acc %= M
    cnt[acc] += 1

res = 0
for i in range(M+1):
    if cnt[i] >= 2:
        tmp = cnt[i]
        res += (tmp * (tmp-1)) // 2

print(res)
