import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0
for i in range(N):
    res += arr[i] * i
    res -= arr[i] * (N-1-i)
print(res*2)