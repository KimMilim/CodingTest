def solution(numbers, hand):
    answer = ''
    
    L = [1,4,7]
    R = [3,6,9]
    M = [2,5,8,0]
    
    pos = {1:[0,0], 2:[0,1], 3:[0,2],
           4:[1,0], 5:[1,1], 6:[1,2],
           7:[2,0], 8:[2,1], 9:[2,2],
                    0:[3,1]}
    
    pos_l = [3,0]
    pos_r = [3,2]
    
    for n in numbers:
        if n in R:
            answer+='R'
            pos_r = pos[n]
        elif n in L:
            answer+='L'
            pos_l = pos[n]
        else:
            dis_r = abs(pos_r[0]-pos[n][0])+abs(pos_r[1]-pos[n][1])
            dis_l = abs(pos_l[0]-pos[n][0])+abs(pos_l[1]-pos[n][1])
            
            if dis_r < dis_l:
                answer+='R'
                pos_r = pos[n]
            elif dis_r > dis_l:
                answer+='L'
                pos_l = pos[n]
            else:
                if hand == 'right':
                    answer+='R'
                    pos_r = pos[n]
                else :
                    answer+='L'
                    pos_l = pos[n]
                
                    
                
            
            
            
            
    
    
    return answer