coins = (500, 100, 50, 10, 5, 1)

r = 1000 - int(input())
cnt = 0
for v in coins:
    cnt += r // v
    r %= v

print(cnt)
