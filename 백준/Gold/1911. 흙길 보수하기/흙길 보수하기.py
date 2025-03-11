import sys
input = sys.stdin.readline

import math

N, L = map(int, input().split())
water = []

for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    water.append((a, b))

water.sort(key=lambda x: x[0])

res = 0
c_max = 0 # 덮인 오른쪽 끝

for st, ed in water:
    if ed <= c_max:
        continue

    start = max(st, c_max)
    distance = ed - start

    cnt = math.ceil(distance / L)
    res += cnt

    c_max = start + cnt * L

print(res)