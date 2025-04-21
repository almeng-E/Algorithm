s = input()
cnt = [0] * 26
for i in s:
    cnt[ord(i)-65] += 1
res = ""
middle = ""
flag = False
for i in range(25, -1, -1):
    if cnt[i] % 2 != 0 and middle:
        res = "I'm Sorry Hansoo"
        flag = True
        break
    elif cnt[i] % 2 != 0 and not middle:
        middle = chr(i+65)

    res += chr(i+65) * (cnt[i] // 2)
if not flag:
    res = res[::-1] + middle + res
print(res)