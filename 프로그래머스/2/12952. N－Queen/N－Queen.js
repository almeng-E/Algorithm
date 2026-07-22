function solution(n) {
    let answer = 0;
    
    const R = Array.from({length: n}, ()=>false);
    const C = Array.from({length: n}, ()=>false);
    const D1 = Array.from({length: 2*n}, ()=>false);
    const D2 = Array.from({length: 2*n}, ()=>false);
    
    nq(0, n);
    
    function nq(x, left) {
        if (left === 0) {
            answer++;
            return;
        }
        
        for (let y=0; y<n; ++y) {
            if (R[x] || C[y] || D1[x+y] || D2[x-y]) continue;
            R[x] = true;
            C[y] = true;
            D1[x+y] = true;
            D2[x-y] = true;
            
            nq(x+1, left-1);
        
            R[x] = false;
            C[y] = false;
            D1[x+y] = false;
            D2[x-y] = false;
        }
    }
    
    return answer;
}