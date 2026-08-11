def solution(s):
    answer = []
    
    s = s[2:-2].split("},{")  # "1,2,3},{2,1},{1,2,4,3},{2" 
    
    tuples = []
    for item in s:    
        parts = list(map(int, item.split(',')))
        tuples.append(parts)
    
    tuples.sort(key=len)
    
    for tup in tuples:
        for ele in tup:
            if ele not in answer:
                answer.append(ele)
                
    return answer