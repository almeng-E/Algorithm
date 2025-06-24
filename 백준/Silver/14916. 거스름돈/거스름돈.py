
n = int(input())
MAX = n//5

for i in range(MAX, -1, -1):
    tmp = n - i*5
    if not tmp & 1:
        print(i + tmp//2)
        break
else:
    print(-1)

