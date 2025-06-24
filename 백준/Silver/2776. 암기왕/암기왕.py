T = int(input())
for _ in range(T):
    N = int(input())
    note = set(map(int, input().split()))

    M = int(input())
    for i in map(int, input().split()):
        print(1 if i in note else 0)