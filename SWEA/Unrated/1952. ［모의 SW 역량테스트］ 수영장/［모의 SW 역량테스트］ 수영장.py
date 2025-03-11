def make_plan(c_idx, c_price):
    global res
    if c_idx > 11:
        res = min(c_price, res)
        return
    if res < c_price:
        return

    if plans[c_idx] == 0:
        make_plan(c_idx+1, c_price)
    else:
        make_plan(c_idx+1, c_price + plans[c_idx] * price[0])
        make_plan(c_idx+1, c_price + price[1])
        make_plan(c_idx+3, c_price + price[2])


T = int(input())


for TC in range(T):
    price = list(map(int, input().split()))
    plans = list(map(int, input().split()))

    res = price[3]

    make_plan(0, 0)

    print(f'#{TC+1} {res}')