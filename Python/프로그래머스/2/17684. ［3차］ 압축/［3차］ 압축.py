def solution(msg):
    answer = []
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    words = {alpha[i]: i + 1 for i in range(len(alpha))}
    
    i=0
    w=""
    while i < len(msg):
        w = w +msg[i]

        if w not in words:
            if w[:-1]:
                answer.append(words[w[:-1]])
            size = len(words)
            words[w]=size+1
            w=""
        else:
            i+=1
    
    if w:
        answer.append(words[w])
            
    
    return answer