import sys
input = sys.stdin.readline
MOD = 10**9 + 7

Q = int(input())
out = []
for _ in range(Q):
    N = int(input())
    if N == 1:
        out.append('5')
    else:
        out.append(str((4 * pow(5, N-1, MOD)) % MOD))

sys.stdout.write('\n'.join(out))
