cnt = 0
for _ in range(6):
    if input() == 'W':
        cnt += 1

if cnt == 0:
    print(-1)
elif cnt == 1 or cnt == 2:
    print(3)
elif cnt == 3 or cnt == 4:
    print(2)
else:
    print(1)