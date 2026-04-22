import heapq

def solution(scoville, K):
    answer = 0
    h=[]
    for i in scoville:
        heapq.heappush(h,i)
    while h[0]<K:
        if len(h)==1:
            return -1
        x1=heapq.heappop(h)
        x2=heapq.heappop(h)
        
        heapq.heappush(h,x1+x2*2)
        answer+=1
    
    
    
    return answer