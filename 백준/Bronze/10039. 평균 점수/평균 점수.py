s = 0
for _ in range(5): 
    a = int(input())
    if a < 40:
        a = 40
    s += a
print(s//5)