import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


PW = input().rstrip()
MOD = 1_000_000

memo = {}   # <str>left_pw : <int>cnt
for i in range(1, 10):
    memo[str(i)] = 1
memo[""] = 1
memo["0"] = 0


def find(cur):
    if cur in memo:
        return memo[cur]

    tmp = 0
    tmp += (find(cur[0]) * find(cur[1:])) % MOD

    if len(cur) >= 2 and 10 <= int(cur[:2]) <= 26:
        tmp += find(cur[2:]) % MOD

    memo[cur] = tmp % MOD
    return memo[cur]

res = find(PW)
print(res)

