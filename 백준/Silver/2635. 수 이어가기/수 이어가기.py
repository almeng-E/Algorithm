N = int(input())

res = []
for i in range(N, (N//2)-1, -1):
    a, b = N, i
    tmp_list = [a, b]
    while True:
        a, b = b, a-b

        if b < 0:
            break

        tmp_list.append(b)

    if len(res) < len(tmp_list):
        res = tmp_list[:]

print(len(res))
print(*res)