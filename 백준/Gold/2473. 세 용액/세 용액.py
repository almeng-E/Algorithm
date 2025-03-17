import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()


min_val = float('inf')
result = []

# mid 기준으로 양 쪽 탐색
for mid in range(1, N-1):
    left = 0
    right = N-1

    while left < mid < right:
        raw_tmp = arr[left] + arr[mid] + arr[right]
        tmp = abs(raw_tmp)
        if tmp == 0:
            result = [arr[left], arr[mid], arr[right]]
            break
        if min_val > tmp:
            min_val = tmp
            result = [arr[left], arr[mid], arr[right]]

        if raw_tmp < 0:
            left += 1
        else:
            right -= 1

print(*result)