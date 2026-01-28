import sys
input = sys.stdin.readline
S1 = input().rstrip()
S2 = input().rstrip()

DP = [[0 for _ in range(len(S2) + 1)] for _ in range(len(S1) + 1)]
for i in range(len(S1)):
    for j in range(len(S2)):
        if S1[i] == S2[j]:
            DP[i+1][j+1] = DP[i][j] + 1
        else:
            DP[i+1][j+1] = max(DP[i][j+1], DP[i+1][j])
print(DP[-1][-1])