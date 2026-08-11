def solution(record):
    answer = []
    
    users={}
    for log in record:
        log_list = list(log.split())
        act = log_list[0]
        
        if act == "Enter" or act == "Change":
            user = log_list[1]
            nick = log_list[2]
            users[user]=nick
    
    for log in record:
        log_list = list(log.split())
        act = log_list[0]
        user = log_list[1]
        if act == "Enter":
            res = users[user]+"님이 들어왔습니다."
            answer.append(res)
        elif act == "Leave":
            res = users[user]+"님이 나갔습니다."
            answer.append(res)
    
    return answer