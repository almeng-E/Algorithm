N = int(input())

words = []
for _ in range(N):
    words.append(input())

word_length = len(words[0])

res = [0 for _ in range(word_length)]


for j in range(word_length):
    tmp = words[0][j]
    for i in range(N):
        if words[i][j] != tmp:
            res[j] = '?'
            break
    else:
        res[j] = tmp

output = ''.join(res)
print(output)