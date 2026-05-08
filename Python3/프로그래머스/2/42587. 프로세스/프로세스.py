from collections import deque

def solution(priorities, location):
    answer = 0
    
    process = enumerate(priorities) # (i, prior)
    
    process_q = deque(process)
    
    cnt=1
    while True:
        cur = process_q.popleft()
        
        # 방법1: max+lambda
        # if cur[1] < max(process_q, key=lambda x: x[1])[1]:
        
        # 방법2: any
        if any(cur[1] < item[1] for item in process_q):
            process_q.append(cur)
        else:
            if cur[0] == location:
                return cnt
            cnt+=1
        
                
    
    
    return answer