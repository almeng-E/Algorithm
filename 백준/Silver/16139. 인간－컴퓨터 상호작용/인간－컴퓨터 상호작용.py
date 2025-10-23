import sys
input = sys.stdin.readline
def main():
    S = input().rstrip()
    
    memo = [[0 for _ in range(len(S)+1)] for _ in range(26)]
    for i in range(len(S)):
        c = S[i]
        idx = ord(c) - 97
    
        for j in range(26):
            memo[j][i+1] = memo[j][i]
    
        memo[idx][i+1] += 1
    
    out = []
    Q = int(input())
    for _ in range(Q):
        cmd = input().split()
        idx = ord(cmd[0]) - 97
        l, r = int(cmd[1]), int(cmd[2])
    
        out.append(str(memo[idx][r+1] - memo[idx][l]))
    print('\n'.join(out))
    
main()