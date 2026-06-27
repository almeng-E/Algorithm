function solution(cacheSize, cities) {
    let answer = 0;
    const cache = new Set();
    if (cacheSize === 0) {
        return cities.length * 5;
    }
    for (const c of cities) {
        const cur = c.toLowerCase();
        if (cache.has(cur)) {
            // hit
            answer += 1;
            
            cache.delete(cur);
            cache.add(cur);
        }
        else {
            // miss
            answer += 5;
            
            if (cacheSize === cache.size) {
                cache.delete(cache.values().next().value);
            }
            cache.add(cur);
            
        }
        
        
    }
    
    
    
    return answer;
}