import sys
input = sys.stdin.readline

from collections import deque

is_prime = [True] * 10000
is_prime[0] = is_prime[1] = False
for i in range(2, 100):
    if is_prime[i]:
        for j in range(i * i, 10000, i):
            is_prime[j] = False

T = int(input())
ans = []
for _ in range(T):
    bef, aft = list(map(int, input().split()))
    ret = 10000

    q = deque()
    v = [False] * 10000
    q.append((bef, 0))
    v[bef] = True
    while q:
        cur, cnt = q.popleft()
        if cur == aft:
            ret = min(cnt, ret)
            break

        cur_str = list(str(cur))
        for i in range(4):
            original_digit = cur_str[i]
            for j in '0123456789':
                if j == original_digit:
                    continue
                cur_str[i] = j
                nxt = int("".join(cur_str))
                if 1000 <= nxt < 10000 and not v[nxt] and is_prime[nxt]:
                    v[nxt] = True
                    q.append((nxt, cnt+1))
            cur_str[i] = original_digit

    if ret == 10000:
        ans.append('Impossible')
    else:
        ans.append(str(ret))
print('\n'.join(ans))