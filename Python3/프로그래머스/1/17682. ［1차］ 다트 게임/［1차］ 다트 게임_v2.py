import re

def solution(dartResult):
    # 1. 정규표현식을 사용하여 (점수)(보너스)(옵션) 패턴 분리
    # (\d+) : 숫자 (10 포함)
    # ([SDT]) : S, D, T 중 하나
    # ([*#]?) : * 또는 #이 올 수도 있고 안 올 수도 있음
    patterns = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    
    scores = []
    bonus_map = {'S': 1, 'D': 2, 'T': 3}
    
    for score, bonus, option in patterns:
        # 보너스 계산
        curr_score = int(score) ** bonus_map[bonus]
        
        # 옵션 계산
        if option == '*':
            curr_score *= 2
            if scores:  # 이전 점수가 있다면 2배 처리
                scores[-1] *= 2
        elif option == '#':
            curr_score *= -1
            
        scores.append(curr_score)
        
    return sum(scores)
