N = int(input())
p = [int(input()) for _ in range(N)]
sp = sorted(p)
if p[0] == sp[0]:
    print('ez')
elif p[0] == sp[-1]:
    print('hard')
else:
    print('?')
