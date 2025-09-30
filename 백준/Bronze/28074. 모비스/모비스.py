S = input()
target = {"M", "O", "B", "I", "S"}
cnt = set()
for c in S:
    if c in target:
        cnt.add(c)
if len(cnt) == len(target):
    print("YES")
else:
    print("NO")