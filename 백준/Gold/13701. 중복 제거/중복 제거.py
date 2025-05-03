import sys
buff = bytearray(33554432//8 + 1)
num = 0
while True:
    b = sys.stdin.buffer.read(1)
    if b != b' ' and b != b'\n':
        num = num*10 + int(b)
    else:
        idx, off = divmod(num, 8)
        if not buff[idx] & (1 << off):
            print(num, end=' ')
            buff[idx] |= (1 << off)
        num = 0
    if b == b'\n':
        break