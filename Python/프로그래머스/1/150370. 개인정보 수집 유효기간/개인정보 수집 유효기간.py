def solution(today, terms, privacies):
    
    def to_days(date):
        y, m, d = map(int, date.split('.'))
        return y * 12 * 28 + m * 28 + d
    
    
    term_dict = {}
    for term in terms:
        name, months = term.split()
        term_dict[name] = int(months)
    
    today_days = to_days(today)
    answer = []
    
    for i, privacy in enumerate(privacies):
        date, name = privacy.split()
        collected = to_days(date)
        expire = collected + term_dict[name] * 28  # 만료 시작일
        
        # expire일부터 파기해야 하므로 today >= expire 이면 파기
        if today_days >= expire:
            answer.append(i + 1)
    
    return answer