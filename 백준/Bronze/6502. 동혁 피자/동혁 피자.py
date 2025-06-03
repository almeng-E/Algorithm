tc = 1
while True:
    cmd = list(map(int, input().split()))

    if cmd[0] == 0:
        break

    r, w, l = cmd
    if 2*r >= (w**2 + l**2) ** 0.5:
        print(f'Pizza {tc} fits on the table.')
    else:
        print(f'Pizza {tc} does not fit on the table.')
    tc += 1