N = int(input())
L = input()
hsh = 0

for i in range(N):
    hsh += ((ord(L[i])-96) * pow(31, i, 1234567891)) % 1234567891
print(hsh%1234567891)