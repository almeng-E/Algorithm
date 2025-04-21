s = input()
for i in s:
    a = ord(i)-3
    if a < 65:
        a += 26
    print(chr(a), end="")