import sys
input = sys.stdin.readline

N = int(input())
pairs = set()

for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    pairs.add((a, b))

fox = {(1, 3), (1, 4), (3, 4)}

if pairs == fox:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")