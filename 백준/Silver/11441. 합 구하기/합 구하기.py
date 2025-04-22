import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))


sum_arr = [0, arr[0]]
for i in range(1, N):
    sum_arr.append(sum_arr[i] + arr[i])

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i-1])