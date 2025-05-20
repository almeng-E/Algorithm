from collections import Counter
i = 1
while True:
    cmd = input()
    if cmd == 'END':
        break
    key = Counter(cmd)
    alpha = Counter(input())
    
    if key == alpha:
        ret = 'same'
    else:
        ret = 'different'

    print(f'Case {i}: {ret}')
    i += 1