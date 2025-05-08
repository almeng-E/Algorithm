N = int(input())
bit = (1<<32) - N
res = 0
for i in range(32):
    if (bit & (1 << i)) != (N & (1 << i)):
        res += 1
print(res)