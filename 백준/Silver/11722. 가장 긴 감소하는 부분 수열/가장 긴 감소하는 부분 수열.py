def bin_search(target):
    left = 0
    right = len(lds) - 1
    while left <= right:
        middle = (left + right) // 2

        if lds[middle] > target:
            left = middle + 1
        else:
            right = middle - 1
    return left



N = int(input())
arr = list(map(int, input().split()))

lds = []
lds.append(arr[0])
for i in range(1, N):
    if lds[-1] > arr[i]:
        lds.append(arr[i])

    else:
        idx = bin_search(arr[i])
        lds[idx] = arr[i]
print(len(lds))