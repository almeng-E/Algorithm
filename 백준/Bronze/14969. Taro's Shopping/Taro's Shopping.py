import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    arr = list(map(int, input().split()))
    arr.sort()

    left = 0
    right = n - 1
    answer = -1

    while left < right:
        total = arr[left] + arr[right]
        if total <= m:
            answer = max(answer, total)
            left += 1
        else:
            right -= 1

    if answer == -1:
        print("NONE")
    else:
        print(answer)