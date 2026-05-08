def solution(s):   
    open_list=[]
    
    for c in s:
        if c=='(':
            open_list.append('(')
        else:
            if not open_list:
                return False
            open_list.pop()

    if open_list: 
        return False
    
    return True