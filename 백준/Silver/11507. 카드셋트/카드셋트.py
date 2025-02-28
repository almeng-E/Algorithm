card_dict = dict()
for key in ("P", "K", "H", "T"):
    card_dict[key] = set(i for i in range(1, 14))

flag = True
str_input = input()
for i in range(0, len(str_input), 3):
    try:
        card_dict[str_input[i]].remove(int(str_input[i+1:i+3]))
    except KeyError:
        flag = False
        print('GRESKA')
        break


if flag:
    for cards in card_dict.values():
        print(len(cards))