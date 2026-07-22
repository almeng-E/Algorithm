function solution(n, computers) {
    let answer = 0;
    
    // dfs
    function dfs(cur) {
        for (let nxt=0; nxt<n; ++nxt) {
            if (!V[nxt] && (computers[cur][nxt] === 1)) {
                V[nxt] = true;
                dfs(nxt);                
            }
        }
    }
    
    const V = Array.from({length: n}, ()=> false);
    for (let i=0; i<n; ++i) {
        if (!V[i]) {
            V[i] = true;
            dfs(i, -1);
            answer++;
        }
    }
    return answer;
}