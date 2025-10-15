G = int(input())

res = []
for i in range(1, G+1):
    if i*i > G:
        break

    if G % i == 0:
        apb = G//i
        amb = i

        if (apb + amb) % 2 == 0 and apb != amb:
            a = (apb + amb) // 2
            res.append(str(a))

print('\n'.join(sorted(res, key=int)) if res else -1)