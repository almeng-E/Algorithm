import sys
input = sys.stdin.readline


def solve():
    N, C = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    
    l, r = 0, N-1
    while l <= r:
        m = (l+r) >> 1
        if arr[m] == C:
            return 1
        elif arr[m] < C:
            l = m+1
        else:
            r = m-1

    l, r = 0, N-1
    while l < r:
        s = arr[l] + arr[r]
        if s == C:
            return 1
        elif s < C:
            l += 1
        else:
            r -= 1

    for i in range(N):
        tg = C - arr[i]
        l, r = i+1, N-1
        while l < r:
            s = arr[l] + arr[r]
            if s == tg:
                return 1
            elif s < tg:
                l += 1
            else:
                r -= 1
    return 0

print(solve())