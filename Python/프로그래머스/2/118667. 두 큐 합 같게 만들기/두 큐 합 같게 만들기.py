from collections import *

def solution(queue1, queue2):
    answer = -1
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if (sum1+sum2)%2: 
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    cnt=0
    while sum1 != sum2 and sum1>=0 and sum2 >=0:
        if cnt >= 600000: break
        
        if sum1 > sum2:
            tmp1 = queue1.popleft()
            sum1-=tmp1
            queue2.append(tmp1)
            sum2+=tmp1
        else :
            tmp2 = queue2.popleft()
            sum2-=tmp2
            queue1.append(tmp2)
            sum1+=tmp2
            
        
        cnt+=1
    
    if cnt >= 600000:
        return -1
    
    return cnt