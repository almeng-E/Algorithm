T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    ON = True
    for i in range(N):
        if M & 1 << i:
            continue
        else:
            ON = False
            break
    print(f'#{TC}', 'ON' if ON else 'OFF')