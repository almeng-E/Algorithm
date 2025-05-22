T = int(input())
for TC in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))


    curr_max = 0
    res = 0
    for i in range(N-1, -1, -1):
        if curr_max < price[i]:
            curr_max = price[i]
        else:
            res += curr_max - price[i]

    print(f'#{TC} {res}')