while True:
    i = input().split()
    if i[0]=='#':
        break
    print(i[0], end=' ')
    if int(i[1]) > 17 or int(i[2])>=80:
        print('Senior')
    else:
        print('Junior')