def power(base, exponent):
    if exponent == 0:
        return 1

    if exponent & 1:
        return base * (power(base, exponent//2) ** 2)
    else:
        return power(base, exponent//2) ** 2


for _ in range(10):
    TC = int(input())
    N, M = map(int, input().split())
    print(f'#{TC} {power(N, M)}')