res = 0
for i in range(3, 0, -1):
    a = input()
    if a.isdigit():
        res = int(a)+i
        break
if res%5 == 0 and res%3 == 0:
    print("FizzBuzz")
elif res%3 == 0 and res%5 != 0:
    print('Fizz')
elif res%3 != 0 and res %5 == 0:
    print("Buzz")
else:
    print(res)