def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0: 
        return len(cities)*5
    
    time=0
    cache=[]
    
    for city in cities:
        city = city.lower()
        if cache and city in cache:
            cache.remove(city)
            cache.append(city)
            time+=1
        elif cache and len(cache) >= cacheSize:
            cache.pop(0)
            cache.append(city)
            time+=5
        else:
            cache.append(city)
            time+=5
    
    return time