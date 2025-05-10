target = 'SciComLove'
res = 0
word = input()
for i in range(10):
    if word[i] != target[i]:
        res += 1
print(res)