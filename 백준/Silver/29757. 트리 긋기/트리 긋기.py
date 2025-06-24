N = int(input())
used = {}
coord = []
for i in range(1, N+1):
    a, b = map(int, input().split())
    coord.append((a, b, i))

coord.sort()


for i in range(N-1):
    print(coord[i][2], coord[i+1][2])