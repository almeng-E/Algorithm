num = int(input())
cnt = 1
while True:
    if num == 1:
        break
    cnt += 1
    if num&1:
        num = 3*num + 1
    else:
        num //= 2
print(cnt)