from collections import defaultdict

N = int(input())

alpha_sum_dict = defaultdict(int)
num = 9

res = 0

for _ in range(N):
    word = input()
    power = len(word)-1
    for letter in word:
        alpha_sum_dict[letter] += (10**power)
        power -= 1


li = list(alpha_sum_dict.items())
li.sort(key=lambda x:x[1], reverse=True)
for _, i in li:
    res += i*num
    num -= 1

print(res)