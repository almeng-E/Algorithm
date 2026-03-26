import sys
input = sys.stdin.readline

from bisect import bisect_left

N, C = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


def solve():
    b = bisect_left(arr, C)
    if b < N and arr[b] == C:
        return 1

    for i in range(N):
        tg = C - arr[i]
        b = bisect_left(arr, tg, i+1)
        if b < N and arr[b] == tg:
            return 1

        for j in range(i+1, N):
            tg = C - arr[i] - arr[j]
            b = bisect_left(arr, tg, j+1)
            if b < N and arr[b] == tg:
                return 1
    return 0


print(solve())