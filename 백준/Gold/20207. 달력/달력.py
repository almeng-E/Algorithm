import sys
input = sys.stdin.readline

N = int(input())

diff = [0] * 367
for _ in range(N):
    s, e = map(int, input().split())
    diff[s] += 1
    diff[e+1] -= 1

ans = 0
cur_len = 0
cur_max = 0
for i in range(1, 367):
    diff[i] += diff[i-1]
    if diff[i] == 0:
        ans += cur_max * cur_len
        cur_len = 0
        cur_max = 0
    else:
        cur_len += 1
        cur_max = max(cur_max, diff[i])
print(ans)