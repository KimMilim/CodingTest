from collections import *

def solution(id_list, report, k):
    answer = []

    report_list = defaultdict(set)
    for s in report:
        f,t=s.split()
        report_list[f].add(t)
    
    
    cnt = defaultdict(int)
    for _,v in report_list.items():
        for vv in v:
            cnt[vv]+=1
    
    report_id=[]
    
    for id in id_list:
        if cnt[id] >= k:
            report_id.append(id)
            
    
    for id in id_list:
        sum=0
        for i in report_list[id]:
            if i in report_id:
                sum+=1
        answer.append(sum)
                
    
        
    return answer