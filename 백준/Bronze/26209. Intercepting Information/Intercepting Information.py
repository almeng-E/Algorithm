s = list(map(int, input().split()))
for c in s:
    if c == 0 or c == 1:
        continue
    else:
        print('F')
        break
else:
    print('S')