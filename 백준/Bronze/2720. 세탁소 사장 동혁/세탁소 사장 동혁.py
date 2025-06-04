T = int(input())

coins = (25, 10, 5, 1)
for _ in range(T):
    v = int(input())
    arr = []
    for i in coins:
        arr.append(v//i)
        v%=i
    print(*arr)