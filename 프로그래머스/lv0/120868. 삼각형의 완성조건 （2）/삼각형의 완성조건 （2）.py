def solution(sides):
    sides.sort()
    if (sides[1]-sides[0])==0:
        a= sum(sides)-1
    else:
        a= 2*sides[0] -1
    return a
        