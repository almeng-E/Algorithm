import sys
data = sys.stdin.buffer.read()

total = 0
N = 0
cur = 0

idx = 0
while 48 <= data[idx] <= 57:
    N *= 10
    N += data[idx] - 48
    idx += 1

while idx < len(data):
    if 48 <= data[idx] <= 57:
        cur *= 10
        cur += data[idx] - 48
    else:
        total += cur
        cur = 0
    idx += 1
total += cur

print(total - (N * (N-1) // 2))