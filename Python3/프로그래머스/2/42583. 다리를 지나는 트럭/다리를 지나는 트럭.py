from collections import *

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    
    t=0
    bridge = deque([0]*(bridge_length))
    trucks = deque(truck_weights)
    
    cur_w=0
    cur_cnt=0
    while trucks or sum(bridge)!=0:

        w = bridge.popleft()
        if w:
            cur_w-=w
            cur_cnt-=1
        
        if cur_cnt + 1<= bridge_length and trucks and cur_w + trucks[0] <=weight:
            bridge.append(trucks[0])
            cur_cnt += 1
            cur_w += trucks[0]
            trucks.popleft()
        else:
            bridge.append(0)
        
        
        # print("t:",t)
        # print("cur_cnt:", cur_cnt, "cur_w:",cur_w)
        # print("bridge:", bridge)
        # print("trucks:", trucks)
        t+=1
    
    return t