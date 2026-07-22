function solution(gems) {
    const N = gems.length;
    let answer = [0, N-1];
    const SZ = new Set(gems).size;
    
    let l = 0;
    let r = 0;
    
    const cnt = new Map();
    
    while (true) {
        if (cnt.size < SZ) {
            if (r === N) break;
            
            const x = gems[r++];
            cnt.set(x, (cnt.get(x) ?? 0) + 1);
            
        }
        else {
            if ((answer[1] - answer[0] + 1) > (r-1 - l + 1)) {
                answer[0] = l;
                answer[1] = r - 1;
            }
            
            const x = gems[l++];
            cnt.set(x, cnt.get(x)-1);
            
            if (cnt.get(x) === 0) {
                cnt.delete(x);
            }
            
                    }
        
    }
    answer[0]++;
    answer[1]++;
    return answer;
}