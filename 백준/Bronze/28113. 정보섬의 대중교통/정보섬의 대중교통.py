N, A, B = map(int, input().split())
if max(N, B) == A:
    print('Anything')
elif max(N, B) > A:
    print('Bus')
else:
    print('Subway')