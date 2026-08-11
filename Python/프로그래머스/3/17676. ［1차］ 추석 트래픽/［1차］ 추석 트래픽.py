from collections import *

def solution(lines):
    answer = 0
    
    calced_lines=[]
    for log in lines:
        _, end_time, times = log.split()
        end_h, end_m, end_s = map(float,end_time.split(':'))
        times = int(float(times[:-1])*1000)
        
        end_time = int((end_h*3600 + end_m*60)*1000 + end_s*1000)
        start_time = int(end_time- times + 1)
        calced_lines.append((start_time, end_time))
        
    
    flag_time=[]
    max_cnt=0
    for s,e in calced_lines:
        flag_time.extend([s,e])
    
    for st in flag_time:
        et = st+999
        cnt=0
        for s,e in calced_lines:
            if e >=st and s <= et:
                cnt+=1
        max_cnt = max(max_cnt, cnt)
        
    
    return max_cnt