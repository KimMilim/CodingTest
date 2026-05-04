import re

def solution(new_id):
    answer = ''
    
    #1
    new_id = new_id.lower()
    
    #2
    new_id = re.sub(r"[^a-z0-9\-_.]","", new_id)
    
    #3
    new_id = re.sub(r"\.{2,}",".", new_id)
    
    #4
    # new_id = re.sub(r"^.","", new_id) --> 아무 글자로 시작해도 ""가 되어버림 --> \써주기
    # new_id = re.sub(r".$","", new_id) --> 아무 글자로 끝나도 ""가 되어버림 --> \써주기
    new_id = re.sub(r"^\.|\.$", "", new_id) #(시작이나 끝의 마침표 제거)
    
    #5
    if new_id=="": 
        new_id = "a"
    #6
    if len(new_id) >= 16:
        new_id = re.sub(r"\.$", "", new_id[:15])
    
    #7
    while len(new_id) <= 2:
        new_id+= new_id[-1]
    
    
    
    
    
    return new_id