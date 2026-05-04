import math
from collections import defaultdict


def transform(time):
    h,m=time.split(':')
    res = int(h)*60+int(m)
    
    return res

def solution(fees, records):
    answer = []
    
    new_records = [ele.split(" ") for ele in records]
    new_records.sort(key = lambda x: (x[1], x[0]))
    

    i=0
    time_dict=defaultdict(int)
    while i< len(new_records):
        cur = new_records[i]
        
        if cur[2]== "IN":
            if i+1 < len(new_records):
                next = new_records[i+1]
                if cur[1] == next[1] and next[2]=="OUT":
                    time_dict[cur[1]] += transform(next[0])-transform(cur[0])
                    i+=2
                else:
                    time_dict[cur[1]] += transform("23:59")-transform(cur[0])
                    i+=1
            else: # 다음이 없음
                time_dict[cur[1]] += transform("23:59")-transform(cur[0])
                break
                
        else:
            i+=1
    
    for c,t in time_dict.items():
        if t <= fees[0]:
            total_fees = fees[1]
        else:
            total_fees = fees[1]
            t-=fees[0]
            total_fees += math.ceil(t/fees[2])*fees[3]
        answer.append(total_fees)
            
                
    
    
    return answer
