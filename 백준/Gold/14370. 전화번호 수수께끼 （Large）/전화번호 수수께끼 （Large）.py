import sys
input = sys.stdin.readline
from collections import defaultdict

a = ['W', 'U', 'X', 'G', 'Z', 'O', 'T', 'F', 'S', 'N']
b = ['TWO', 'FOUR', 'SIX', 'EIGHT', 'ZERO', 'ONE', 'THREE', 'FIVE', 'SEVEN', 'NINE']
c = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9]

T = int(input())
for tc in range(T):
    S = input().rstrip()

    cnt = defaultdict(int)
    for s in S:
        cnt[s] += 1

    ret = []
    for i in range(len(a)):
        while a[i] in cnt and cnt[a[i]] != 0:
            for bb in b[i]:
                cnt[bb] -= 1
            ret.append(c[i])
    ret = ''.join(map(str, sorted(ret)))
    print(f'Case #{tc+1}: {ret}')


'''
# TWO     : T 1 'W 1' O 1
# FOUR    : F 1 O 1 'U 1' R 1
# SIX     : S 1 I 1 'X 1'
# EIGHT   : E 1 I 1 'G 1' H 1 T 1
# ZERO    : 'Z 1' E 1 R 1 O 1

ONE     : O 1 N 1 E 1

THREE   : T 1 H 1 R 1 E 2

FIVE    : F 1 I 1 V 1 E 1

SEVEN   : S 1 E 2 V 1 N 1

NINE    : N 2 I 1 E 1
'''