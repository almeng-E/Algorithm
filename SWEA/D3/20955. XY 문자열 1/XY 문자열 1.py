T = int(input())
for TC in range(T):
    S = list(input().rstrip())
    E = list(input().rstrip())
    while len(E) > len(S):
        if E[-1] == 'X':
            E.pop()
        else:
            E.pop()
            E.reverse()
    if E == S:
        print(f'#{TC+1} Yes')
    else:
        print(f'#{TC+1} No')