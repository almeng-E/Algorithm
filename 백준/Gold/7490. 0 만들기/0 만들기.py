import sys
input = sys.stdin.readline
def backtrack(cur, v, bef, s):
    if cur == N+1:
        if v == 0:
            ans.append(s)
        return

    # ' '
    if bef > 0:
        new_bef = bef * 10 + cur
    else:
        new_bef = bef * 10 - cur
    backtrack(cur+1, v - bef + new_bef, new_bef, s + ' ' + str(cur))

    # +
    backtrack(cur+1, v+cur, cur, s + '+' + str(cur))

    # -
    backtrack(cur+1, v-cur, -cur, s + '-' + str(cur))



T = int(input())
for _ in range(T):
    N = int(input())
    ans = []
    backtrack(2, 1, 1, '1')

    print('\n'.join(ans))
    print()