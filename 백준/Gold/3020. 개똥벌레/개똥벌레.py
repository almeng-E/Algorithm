import sys
input = sys.stdin.readline
N, H = map(int, input().split())

up = []
down = []
flag = 0

for _ in range(N):
    if flag:
        up.append(int(input()))
    else:
        down.append(int(input()))
    flag ^= 1

imos = [0] * (H+1)
for d in down:
    imos[0] += 1
    imos[d+1] -= 1
for i in range(1, H+1):
    imos[i] = imos[i-1] + imos[i]

imos2 = [0] * (H+1)
for u in up:
    imos2[0] += 1
    imos2[u+1] -= 1
for i in range(1, H+1):
    imos2[i] = imos2[i-1] + imos2[i]
for i in range(1, H+1):
    imos[i] += imos2[H-i+1]

min_val = N
min_cnt = 0
for i in range(1, H+1):
    if min_val > imos[i]:
        min_val = imos[i]
        min_cnt = 1
    elif min_val == imos[i]:
        min_cnt += 1
print(min_val, min_cnt)
