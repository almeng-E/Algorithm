T = int(input())


for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    print(f'Scenario #{tc}:')
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('yes')
    else:
        print('no')
    print()