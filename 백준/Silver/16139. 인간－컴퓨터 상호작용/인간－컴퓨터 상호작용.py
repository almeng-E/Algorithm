import sys
input = sys.stdin.readline


S = input().rstrip()

memo = [[] for _ in range(26)]
res = []
for i in range(len(S)):
    j = ord(S[i]) - 97
    memo[j].append(i)

Q = int(input())
for _ in range(Q):
    cmd = input().split()
    l, r = int(cmd[1]), int(cmd[2])

    j = ord(cmd[0]) - 97

    # 최적화 : 이진탐색
    lc, rc = -1, -1

    left, right = 0, len(memo[j]) - 1
    while left <= right:
        mid = (left + right) // 2
        if memo[j][mid] < l:
            lc = mid
            left = mid + 1
        else:
            right = mid - 1

    left, right = 0, len(memo[j]) - 1
    while left <= right:
        mid = (left + right) // 2
        if memo[j][mid] <= r:
            rc = mid
            left = mid + 1
        else:
            right = mid - 1

    res.append(str(rc - lc))
print('\n'.join(res))