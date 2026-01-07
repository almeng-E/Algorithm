t = [0, 0]
for _ in range(2):
    a, b = map(int, input().split())
    t[0] += a
    t[1] += b
if t[0] < t[1]:
    print('Hanyang Univ.')
elif t[0] == t[1]:
    print('Either')
else:
    print('Yongdap')