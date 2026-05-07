from collections import *

def solution(genres, plays):
    answer = []
    
    genre_play = defaultdict(int)
    genre_plays =defaultdict(list)
    
    for i in range(len(plays)):
        genre_play[genres[i]]+=plays[i]
        genre_plays[genres[i]].append(( i,plays[i]))
    
    sorted_play = list((g,c) for g,c in genre_play.items())
    sorted_play.sort(key=lambda x:-x[1])    
    
                           
    for genre,_ in sorted_play:
        tmp = sorted(genre_plays[genre], key=lambda x: -x[1])
        tmp = tmp[:2]
        for i,p in tmp:
            answer.append(i)
            
    
    
    return answer