from collections import *

def solution(phone_book):
    answer = True
    
    
    phone_book.sort(key=lambda x:len(x))
    
    cnt = defaultdict(int)
    for phone in phone_book:
        cnt[phone]+=1
        
        for i in range(1,len(phone)):
            if cnt[phone[:i]] >= 1:
                answer=False
                break
        if not answer:
            break
            
    
    return answer