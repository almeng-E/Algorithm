
N, K, P = map(int, input().split())
res = 0
arr = list(map(int, input().split()))
for i in range(N):
    cnt = 0
    for j in range(K):
        if not arr[i*K+j]:
            cnt += 1
    if cnt < P:
        res += 1

print(res)

