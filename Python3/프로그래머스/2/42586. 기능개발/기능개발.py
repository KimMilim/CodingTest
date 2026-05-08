import math

def solution(progresses, speeds):
    answer = []
    
    n = len(progresses)
    st = []
    
    for i in range(n):
        day = math.ceil((100-progresses[i])/speeds[i])
        
        if not st or max(st) >= day:
            st.append(day)
        else:
            answer.append(len(st))
            st.clear()
            st.append(day)
    
    if st:
        answer.append(len(st))
    return answer