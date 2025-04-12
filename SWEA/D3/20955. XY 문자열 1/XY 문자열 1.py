T = int(input())
for TC in range(T):
    S = input().rstrip()
    E = input().rstrip()

    is_reversed = 0

    while len(S) < len(E):
        if not is_reversed:
            if E[-1] == 'X':
                E = E[:-1]
            else:
                E = E[:-1]
                is_reversed ^= 1
        else:
            if E[0] == 'X':
                E = E[1:]
            else:
                E = E[1:]
                is_reversed ^= 1
    if is_reversed:
        E = E[::-1]

    if E == S:
        print(f'#{TC+1} Yes')
    else:
        print(f'#{TC+1} No')