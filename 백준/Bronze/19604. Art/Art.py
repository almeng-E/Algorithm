minx, miny = 101, 101
maxx, maxy = -1, -1


N = int(input())
for _ in range(N):
    a, b = map(int, input().split(','))
    minx = min(minx, a)
    maxx = max(maxx, a)
    miny = min(miny, b)
    maxy = max(maxy, b)

print(f'{minx-1},{miny-1}')
print(f'{maxx+1},{maxy+1}')