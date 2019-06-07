def solution(cacheSize, cities):
    cache = []
    length = 0
    time = 0
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in cache:
            # cache hit
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            # cache miss
            time += 5
            if length < cacheSize:
                cache.append(city)
                length += 1
            else:
                cache.pop(0)
                cache.append(city)
    return time

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities)) # 50
cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize, cities)) # 21
cacheSize = 2
cities = 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize, cities)) # 60
cacheSize = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize, cities)) # 52
cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities)) # 16
cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities)) # 25