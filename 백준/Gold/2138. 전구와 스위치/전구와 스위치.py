N = int(input())

a = list(map(int, input()))
b = list(map(int, input()))

lamp = 0
target = 0
for i in range(N):
    if a[i]:
        lamp |= (1 << i)
    if b[i]:
        target |= (1 << i)

전구 = lamp
cnt_a = 0
# 첫번째 안누름
for i in range(1, N):
    if 전구 == target:
        break
    if (전구 & (1 << (i-1))) != (target & (1 << (i-1))):
        cnt_a += 1
        전구 ^= (1 << i-1)
        전구 ^= (1 << i)
        if i+1 < N:
            전구 ^= (1 << i+1)
if 전구 != target:
    cnt_a = float('inf')


# 첫번째 누름
전구 = lamp
전구 ^= (1 << 0)
전구 ^= (1 << 1)
cnt_b = 1
for i in range(1, N):
    if 전구 == target:
        break
    if (전구 & (1 << (i-1))) != (target & (1 << (i-1))):
        cnt_b += 1
        전구 ^= (1 << i-1)
        전구 ^= (1 << i)
        if i+1 < N:
            전구 ^= (1 << i+1)
if 전구 != target:
    cnt_b = float('inf')

res = min(cnt_a, cnt_b)
print(res if res != float('inf') else -1)