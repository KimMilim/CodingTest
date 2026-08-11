from collections import defaultdict

def solution(survey, choices):
    score = defaultdict(int)
    for (a, b), choice in zip(survey, choices):
        score[a if choice < 4 else b] += abs(choice - 4)
    
    return ''.join(a if score[a] >= score[b] else b 
                   for a, b in [('R','T'),('C','F'),('J','M'),('A','N')])
