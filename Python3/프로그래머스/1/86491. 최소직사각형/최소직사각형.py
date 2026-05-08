def solution(sizes):
    answer = 0
    
    row=[]
    col=[]
    
    for ele in sizes:
        row.append(max(ele))
        col.append(min(ele))
        
    answer = max(row)*max(col)
    
    return answer