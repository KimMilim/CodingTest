def solution(str1, str2):
    answer = 0
    
    list1=[]
    list2=[]
    
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha()==True: 
            list1.append(str1[i:i+2].lower())
    
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha() == True:
            list2.append(str2[i:i+2].lower())
    
    
    resset = set(list1+list2)
    
    interset = []
    unionset = []
    
    for ele in resset:
        min_cnt = min(list1.count(ele), list2.count(ele))
        max_cnt = max(list1.count(ele), list2.count(ele))
        
        for _ in range(min_cnt):
            interset.append(ele)
            
        for _ in range(max_cnt):
            unionset.append(ele)
        
            
    if len(interset)==0 and len(unionset) ==0:
        return 65536
    
    res = int(len(interset)/len(unionset)*65536)
    
    
    return res