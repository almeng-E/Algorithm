import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
def 부분팰린드롬체크(start, end):
    if memo[start][end] != -1:
        return memo[start][end]

    if start >= end:
        memo[start][end] = 1
        return 1

    if arr[start] != arr[end]:
        memo[start][end] = 0
        return 0

    if 부분팰린드롬체크(start + 1, end - 1) == 1:
        memo[start][end] = 1
        return 1
    else:
        memo[start][end] = 0
        return 0

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

# memo[시작 idx][끝 idx]
memo = [[-1 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    print(부분팰린드롬체크(s, e))
