function solution(strs, t) {
    let answer = 0;
    const N = t.length;
    
    const wSet = new Set(strs);
    
    const dp = Array.from({length: N+1}, ()=>Infinity);
    dp[0] = 0;
    for (let i=1; i<=N; ++i) {
        for (let len=1; len<=5; ++len) {
            if (i-len < 0) break;
            const piece = t.slice(i-len, i);
            
            if (!wSet.has(piece)) continue;
            
            dp[i] = Math.min(dp[i], dp[i-len]+1);
        }
    }
    if (dp[N] === Infinity) answer = -1;
    else answer = dp[N];
    
    return answer;
}