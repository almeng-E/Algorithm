import sys
input = sys.stdin.readline

N = int(input())

pos_nums = []
neg_nums = []

res = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        pos_nums.append(num)
    elif num <= 0:
        neg_nums.append(num)
    else:
        res += 1

pos_nums.sort(reverse=True)
neg_nums.sort()


for i in range(0, len(pos_nums), 2):
    if i+1 >= len(pos_nums):
        res += pos_nums[i]
    else:
        res += (pos_nums[i] * pos_nums[i+1])


for i in range(0, len(neg_nums), 2):
    if i+1 >= len(neg_nums):
        res += neg_nums[i]
    else:
        res += (neg_nums[i] * neg_nums[i+1])

print(res)
