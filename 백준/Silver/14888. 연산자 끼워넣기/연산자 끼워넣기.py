def recursive(tmp, idx):
    global min_value, max_value, add, sub, mul, div

    if idx == N:
        min_value = min(tmp, min_value)
        max_value = max(tmp, max_value)
        return

    if add > 0:
        add -= 1
        recursive(tmp + NUMS[idx], idx+1)
        add += 1
    if sub > 0:
        sub -= 1
        recursive(tmp - NUMS[idx], idx+1)
        sub += 1
    if mul > 0:
        mul -= 1
        recursive(tmp * NUMS[idx], idx+1)
        mul += 1
    if div > 0:
        div -= 1
        recursive(int(tmp/NUMS[idx]), idx+1)
        div += 1

max_value, min_value = -1 * 1e10, 1e10

N = int(input())
NUMS = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())


recursive(NUMS[0], 1)


print(max_value)
print(min_value)