import sys
input = sys.stdin.readline

ln = [0] * 26

for _ in range(int(input())):
    ln[ord(input()[0]) - 97] += 1

res = ''
for i in range(26):
    if ln[i] >= 5:
        res += chr(i + 97)
print(res if res else 'PREDAJA')