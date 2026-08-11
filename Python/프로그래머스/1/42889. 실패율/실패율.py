def solution(N, stages):
    answer = []
    
    cnt = [0]*(N+2)
    
    for s in stages:
        cnt[s]+=1
        
    # for c in cnt:
    #     print(c)
    
    size = len(stages)
    
    
    fail_dict={}
    for i in range(1,len(cnt)-1):
        if size == 0: 
            fail_dict[i] = 0
        else:
            fail_dict[i] = cnt[i]/size
        # print(i, ":", fail_dict[i])
        size -= cnt[i]
    

    sorted_fail = sorted(fail_dict.items(), key=lambda x: (-x[1], x[0]))
    
    
    answer = [x for x,v in sorted_fail]    
    
    
    return answer