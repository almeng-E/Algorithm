def vpsCheck(str):
    a=0
    for i in str:
        if i == "(": 
            a+=1
        elif i== ")": 
            a-=1
            if a<0: 
                return "NO"
        else: 
            continue
    if a==0: 
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    result=vpsCheck(input())
    print(result)