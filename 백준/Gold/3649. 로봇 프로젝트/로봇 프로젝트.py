import sys
input = sys.stdin.readline


while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        lego = [int(input()) for _ in range(n)]

        lego.sort()
        res = (-1, -1)

        for i in range(n-1):
            key = lego[i]
            target = x - key

            left = i+1
            right = n-1

            while left <= right:
                mid = (left + right) // 2

                if lego[mid] < target:
                    left = mid + 1
                elif lego[mid] == target:
                    if abs(res[0] - res[1]) <= abs(key - target):
                        res = (key, target)
                    break
                else:
                    right = mid - 1

        if res[0] == -1:
            print('danger')
        else:
            print(f'yes {res[0]} {res[1]}')
    except:
        break