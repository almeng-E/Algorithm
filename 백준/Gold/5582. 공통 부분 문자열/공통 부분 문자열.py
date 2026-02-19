import sys
input = sys.stdin.readline
def solve():
    S1 = input().rstrip()
    S2 = input().rstrip()
    ans = 0
    bef = [0] * (len(S1)+1)
    for i in range(len(S2)):
        cur = [0] * (len(S1)+1)
        for j in range(len(S1)):
            if S1[j] == S2[i]:
                cur[j+1] = bef[j] + 1
                ans = max(ans, cur[j+1])
        bef = cur
    print(ans)
solve()