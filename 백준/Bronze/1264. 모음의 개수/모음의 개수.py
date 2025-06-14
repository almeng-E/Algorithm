vowels = {'a','e','i','o','u','A','E','I','O','U'}
while True:
    r = 0
    s = input()
    if s == '#':
        break
    for i in s:
        if i in vowels:
            r += 1
    print(r)