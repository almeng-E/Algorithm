import sys

class_sum=0
score_sum=0.0

score_li=["F",0,"D0","D+","C0","C+","B0","B+","A0","A+"]

for _ in range(20):
    _,a,b = sys.stdin.readline().split()
    if b=="P":
        continue
    a=float(a)
    class_sum+=a
    score_sum+=a * score_li.index(b)/2
print('%.6f'%(score_sum/class_sum))
    


