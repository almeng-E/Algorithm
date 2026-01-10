import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[1]-x[0])
print(0 if arr[K-1][1] - arr[K-1][0] <= 0 else arr[K-1][1] - arr[K-1][0])