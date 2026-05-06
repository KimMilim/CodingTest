def solution(record):
    user_db = {}
    actions = []
    
    # 메시지 템플릿 정의
    printer = {
        "Enter": "님이 들어왔습니다.",
        "Leave": "님이 나갔습니다."
    }

    # 1. 최신 닉네임 업데이트 및 액션 로그 저장
    for log in record:
        split_log = log.split()
        act, uid = split_log[0], split_log[1]
        
        # 닉네임 정보가 있는 경우(Enter, Change) 업데이트
        if len(split_log) > 2:
            user_db[uid] = split_log[2]
        
        # 출력 대상인 액션만 따로 저장 (Change 제외)
        if act in printer:
            actions.append((act, uid))

    # 2. 저장된 로그를 바탕으로 최종 메시지 생성
    return [f"{user_db[uid]}{printer[act]}" for act, uid in actions]
