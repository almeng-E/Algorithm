import sys

buff = bytearray((1 << 25)//8)

s = ''
while True:
    c = sys.stdin.read(1)
    if c.isnumeric():
        s += c
    else:

        num = int(s)
        idx = num // 8
        off = num % 8
        if not buff[idx] & (1 << off):
            print(num, end=' ')
            buff[idx] |= (1 << off)
        s = ''
        if c != ' ':
            break