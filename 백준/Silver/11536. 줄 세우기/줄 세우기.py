import sys
input = sys.stdin.readline
N = int(input())
names = [input().rstrip() for _ in range(N)]
if names[0] < names[1]:
    for i in range(1, N-1):
        if names[i] >= names[i+1]:
            print('NEITHER')
            break
    else:
        print('INCREASING')
else:
    for i in range(1, N - 1):
        if names[i] <= names[i + 1]:
            print('NEITHER')
            break
    else:
        print('DECREASING')