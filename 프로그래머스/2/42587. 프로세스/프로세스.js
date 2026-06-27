function solution(priorities, location) {
    let answer = 0;
    
    const N = priorities.length;
    const P = [...priorities].sort((a, b) => b-a);
    let P_idx = 0;
    
    const used = new Array(N).fill(false);
    let cur_idx = 0;
    
    while (P_idx < N) {
        if (!used[cur_idx] && (P[P_idx] === priorities[cur_idx])) {
            P_idx++;
            used[cur_idx] = true;
            if (cur_idx === location) return P_idx;
        }
        cur_idx++;
        cur_idx%=N;
    }
    
    
    return answer;
}