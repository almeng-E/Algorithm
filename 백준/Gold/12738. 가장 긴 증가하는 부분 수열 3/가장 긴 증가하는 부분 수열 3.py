def bin_search(target):
    left = 0
    right = len(lis) - 1
    while left <= right:
        middle = (left + right) // 2

        if target > lis[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return left



N = int(input())
arr = list(map(int, input().split()))

lis = []
lis.append(arr[0])


for i in range(1, N):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        # 변경 할 위치를 찾는다
        idx = bin_search(arr[i])
        lis[idx] = arr[i]

print(len(lis))