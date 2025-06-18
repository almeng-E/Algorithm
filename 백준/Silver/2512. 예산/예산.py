import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
budget = int(input())

if budget >= sum(arr):
    print(max(arr))

else:
    left = 0
    right = budget

    while left <= right:
        mid = (left + right) // 2

        tmp = budget
        for v in arr:
            if v <= mid:
                tmp -= v
            else:
                tmp -= mid

        if tmp >= 0:
            left = mid + 1
        else:
            right = mid - 1

    print(right)