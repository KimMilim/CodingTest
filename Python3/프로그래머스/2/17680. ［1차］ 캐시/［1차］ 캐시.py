from collections import *

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0: 
        return len(cities)*5
    
    time=0
    cache=deque(maxlen = cacheSize)
    
    for city in cities:
        city = city.lower()
        if cache and city in cache:
            cache.remove(city)
            cache.append(city)
            time+=1
        
        else:
            cache.append(city)
            time+=5
    
    return time