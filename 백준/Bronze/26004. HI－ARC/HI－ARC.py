N = int(input())
S = input().rstrip()
d = {'H': 0, 'I': 0, 'A': 0, 'R': 0, 'C': 0}
for c in S:
    if c in d:
        d[c] += 1
print(min(d.values()))