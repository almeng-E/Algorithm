lst = []
N = int(input())

for _ in range(N):
    ser = input()
    S = 0
    for i in ser:
        if i.isdigit():
            S += int(i)
    lst.append((S, ser))

lst.sort(key=lambda x: (len(x[1]), x[0], x[1]))
for i in lst:
    print(i[1])