tg = [1,2,3,4,5]
arr = list(map(int, input().split()))
while arr != tg:
    for i in range(4):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)