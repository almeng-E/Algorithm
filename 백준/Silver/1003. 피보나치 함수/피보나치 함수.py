T = int(input())

fibo = [0] * 41
fibo[0] = (1, 0)
fibo[1] = (0, 1)


for _ in range(T):
    N = int(input())
    for i in range(N+1):
        if not fibo[i]:
            st = i
            break
    else:
        print(*fibo[N])
        continue

    for i in range(st, N+1):
        fibo[i] = (fibo[i-2][0] + fibo[i-1][0], fibo[i-2][1] + fibo[i-1][1])

    print(*fibo[N])