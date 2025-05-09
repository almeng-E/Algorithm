s_dict = dict()
N = int(input())

for _ in range(N):
    ser = input()
    L = len(ser)
    S = 0
    for i in ser:
        if i.isdigit():
            S += int(i)
    # L : [S, word]

    if L in s_dict:
        s_dict[L].append((S, ser))
    else:
        s_dict[L] = [(S, ser)]

for key in sorted(s_dict.keys()):
    lst = s_dict[key]
    for i in sorted(lst):
        print(i[1])