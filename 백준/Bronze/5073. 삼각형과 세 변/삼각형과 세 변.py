while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr.sort(reverse=True)

    if arr[0] >= arr[1] + arr[2]:
        print("Invalid")
        continue

    if arr[0] == arr[1] == arr[2]:
        print("Equilateral")
        continue

    if arr[0] != arr[1] and arr[1] != arr[2]:
        print("Scalene")
        continue
    print("Isosceles")