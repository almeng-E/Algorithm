N = int(input())
distance = [0] + list(map(int, input().split()))
price = list(map(int, input().split()))

res = 0

c_index = 0
next_index = 1
while next_index < N:


    res += distance[next_index] * price[c_index]
    # 다음 주유소와 가격 비교
    if price[c_index] > price[next_index]:
        c_index = next_index

    next_index += 1
print(res)