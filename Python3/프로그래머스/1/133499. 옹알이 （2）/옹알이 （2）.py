import re

def solution(babbling):
    answer = 0
    
    word=["aya", "ye", "woo", "ma"]
    
    for baby in babbling:
        
        fail=False
        for w in word:
            if w*2 in baby:
                fail=True
                break
        if fail:
            continue
                
        
        if re.fullmatch(r"(aya|ye|woo|ma)*",baby):
            answer+=1
    
    
    return answer