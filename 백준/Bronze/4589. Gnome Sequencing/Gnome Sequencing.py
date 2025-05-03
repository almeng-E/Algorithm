N = int(input())
print('Gnomes:')

for _ in range(N):
    arr = list(map(int, input().split()))
    if (arr[0] < arr[1] and arr[1] < arr[2]) or (arr[0] > arr[1] and arr[1] > arr[2]):
        print('Ordered')
    else:
        print('Unordered')