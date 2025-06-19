import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    food = sum(map(int, input().split()))
    days = 1
    while food <= N:
        days += 1
        food *= 4
    print(days)