n = int(input())
if n == 1:
    print(1)
else:
    for i in range(2, 10):
        if n%i :
            continue
        elif n//i <= 9:
            print(1)
            break
    else:
        print(0)