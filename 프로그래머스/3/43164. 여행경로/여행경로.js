function solution(tickets) {
    let answer = ['ICN'];
    const N = tickets.length;
    const G = new Map();
    const used = Array.from({length: N}, ()=>false);
    
    for (let i=0; i<N; ++i) {
        const [a, b] = tickets[i];
        if (!G.has(a)) G.set(a, []);
        if (!G.has(b)) G.set(b, []);
        
        G.get(a).push([b, i]);
    }
    
    for (const k of G.keys()) G.get(k).sort();
        
    let found = false;
    
    function backtrack(cur) {
        if (answer.length === N+1) {
            found = true;
            return;
        }
        
        if (found) return;
        
        for (const [v, i] of G.get(cur)) {
            if (!used[i]) {
                used[i] = true;
                answer.push(v);
                backtrack(v);
                
                if (found) return;
                
                answer.pop();
                used[i] = false;
            }
        }
    }    

    backtrack('ICN');
        
    return answer;
}