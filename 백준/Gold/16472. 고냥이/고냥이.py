import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
res = 0
for i in range(len(S)):
    used = set()
    j = i
    while j < len(S):
        if S[j] not in used:
            if len(used) == N:
                break
            else:
                used.add(S[j])
        j += 1
    res = max(res, j-i)

    if j == len(S):
        break

print(res)