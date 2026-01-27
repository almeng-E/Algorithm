import sys
input = sys.stdin.readline
N, D, K = map(int, input().split())
drop = list(map(int, input().split()))
cnt = 0
cur = [0] * N
for i in range(D):
    clean = False
    for j in range(N):
        if cur[j] + drop[j] > K:
            clean = True
            break
    if clean:
        cur = [0] * N
        cnt += 1
    for j in range(N):
        cur[j] += drop[j]
print(cnt)