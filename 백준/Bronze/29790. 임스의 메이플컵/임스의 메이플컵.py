a,b,c=map(int,input().split())
if a<1000:print('Bad')
else:
    if b>=8000 or c>=260:print('Very Good')
    else:print('Good')