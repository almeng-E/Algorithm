function solution(triangle) {
    let answer = 0;
    
    const N = triangle.length;
    
    const DP = [];
    for (let i=1; i<=N; ++i) {
        DP.push(Array.from({length: i}, ()=>0));
    }
    for (let j=0; j<N; ++j) {
        DP[N-1][j] = triangle[N-1][j];
    }
    
    for (let i=N-2; i>=0; --i) {
        for (let j=0; j<=i; ++j) {
            DP[i][j] = triangle[i][j] + Math.max(DP[i+1][j], DP[i+1][j+1]);
        }
    }    
    answer = DP[0][0];
    
    return answer;
}