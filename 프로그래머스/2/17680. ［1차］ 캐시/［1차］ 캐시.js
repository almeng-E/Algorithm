function solution(cacheSize, cities) {
    let answer = 0;
    
    if (cacheSize === 0) return cities.length*5;
    
    const C = new Set();
    
    
    for (let city of cities) {
        city = city.toLowerCase();
        if (C.has(city)) {
            // hit
            answer += 1;
            
            C.delete(city);
            C.add(city);
        }
        else {
            // miss
            answer += 5;
            
            if (C.size === cacheSize) {
                const [nxt] = C;
                C.delete(nxt);
            }
            C.add(city);
        }
    }
    
    return answer;
}