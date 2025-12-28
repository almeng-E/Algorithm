A, B, C, D = map(int, input().split())
s = True if A+B<=D else False
w = True if C<=D else False
if s&w: print('~.~')
elif not s and not w: print('T.T')
elif s: print('Shuttle')
else: print('Walk')