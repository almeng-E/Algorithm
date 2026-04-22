def solution(dots):
    x,y=0,0
    for i in range(1,len(dots)):
        tmpx=abs(dots[i][0]-dots[0][0])
        tmpy=abs(dots[i][1]-dots[0][1])        
        x,y=max(x,tmpx),max(y,tmpy)
    answer = x*y
    return answer