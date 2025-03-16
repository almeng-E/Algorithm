T = int(input())
for TC in range(T):
    N, M = map(int, input().split())


    for i in range(N):
        if M & 1 << i:
            continue
        else:
            print(f'#{TC+1} OFF')
            break
    else:
        print(f'#{TC+1} ON')