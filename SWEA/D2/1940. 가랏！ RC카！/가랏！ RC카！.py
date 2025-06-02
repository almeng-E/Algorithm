T = int(input())
for TC in range(1, T+1):
    N = int(input())
    res = 0
    s = 0
    for _ in range(N):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1:
            s += cmd[1]
        elif cmd[0] == 2:
            s -= cmd[1]
            if s < 0:
                s = 0
        res += s
    print(f'#{TC} {res}')