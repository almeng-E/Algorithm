import sys
input = sys.stdin.readline
from itertools import combinations


def solve():
    N, K = map(int, input().split())

    words = []
    used_letter = 0

    for _ in range(N):
        S = input().rstrip()
        tmp = 0
        for c in S:
            tmp |= (1 << (ord(c) - ord('a')))
            used_letter |= (1 << (ord(c) - ord('a')))
        words.append(tmp)

    if K < 5:
        return 0

    base = 0
    for c in ['a', 'n', 't', 'i', 'c']:
        base |= (1 << (ord(c) - ord('a')))
        used_letter &= ~(1 << (ord(c) - ord('a')))

    cands = []
    for i in range(26):
        if used_letter & (1 << i):
            cands.append(i)
    if len(cands) <= K-5:
        return N

    ans = 0
    nCr = combinations(cands, K-5)
    for comb in nCr:
        cnt = 0
        learned_bits = base
        for c in comb:
            learned_bits |= 1 << (c)
        for w_bits in words:
            if (w_bits & learned_bits) == w_bits:
                cnt += 1
        ans = max(ans, cnt)
    return ans

print(solve())

