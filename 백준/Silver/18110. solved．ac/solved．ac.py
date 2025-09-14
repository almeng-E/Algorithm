import sys
input = sys.stdin.readline

N = int(input())
cut_off = (N * 15 + 50) // 100


arr = [int(input()) for _ in range(N)]
arr.sort()
remain = N - 2 * cut_off
s = sum(arr[cut_off:N - cut_off])
if s != 0:

    print((s * 2 + remain) // (2 * remain))
else:
    print(0)