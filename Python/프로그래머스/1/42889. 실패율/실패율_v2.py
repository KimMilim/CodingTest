from collections import Counter

def solution(N, stages):
    # Counter 이용
    cnt = Counter(stages)
    size = len(stages)
    fail_dict = {}
    
    for i in range(1, N + 1):
        if size > 0:
            fail_dict[i] = cnt[i] / size
            size -= cnt[i]
        else:
            fail_dict[i] = 0
            
    
    return sorted(fail_dict, key=lambda x: (-fail_dict[x], x))
    #return [x for x,v in sorted(fail_dict.items(), key=lambda x: (-x[1], x[0]))]
