def solution(survey, choices):
    answer = ''
    
    
    index = {'RT':0, 'TR':0, 'CF':1, 'FC':1, 'JM':2, 'MJ':2, 'AN':3, 'NA':3}
    score = [{'R':0, 'T':0}, {'C':0, 'F':0}, {'J':0, 'M':0}, {'A':0, 'N':0}]
    
    for i in range(len(survey)):
        type = survey[i]
        num = choices[i]
        
        if num <= 4:
            score[index[type]][type[0]] += (4-num)
        else:
            score[index[type]][type[1]] += (num-4)
    
    for type in score:
        
        tmp = list(type.items())
        # print(tmp)
        tmp.sort(key=lambda x:(-x[1],x[0]))
        answer+=tmp[0][0]
            
        
    
    
    return answer