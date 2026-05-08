def solution(answers):
    res = []
    
    stu = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    sum=[0,0,0]
    
    for i in range(len(answers)):
        for s in range(3):
            sum[s] += 1 if answers[i] == stu[s][i%len(stu[s])] else 0
            
    max_ans = max(sum)
    for j in range(len(sum)):
        if sum[j]==max_ans:
            res.append(j+1)
    
    return res