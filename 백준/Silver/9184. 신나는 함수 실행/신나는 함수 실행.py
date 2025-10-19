import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def w(a, b, c):
    if (a, b, c) in memo:
        return memo[(a, b, c)]
    
    if a<=0 or b<=0 or c<=0:
        memo[(a, b, c)] = 1
    elif a>20 or b>20 or c>20:
        memo[(a, b, c)] = w(20, 20, 20)
    elif a<b and b<c:
        memo[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        memo[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memo[(a, b, c)]


while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break

    memo = dict()
    w(a, b, c)

    print(f'w({a}, {b}, {c}) = {memo[(a, b, c)]}')