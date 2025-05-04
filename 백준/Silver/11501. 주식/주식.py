
T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    res = 0
    max_p = price[-1]
    tmp = 0
    for i in range(N-1, -1, -1):
        if price[i] > max_p:
            res += tmp
            tmp = 0
            max_p = price[i]
        else:
            tmp += (max_p - price[i])
    else:
        if tmp:
            res += tmp

    print(res)
