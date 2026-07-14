function solution(N, M, puddles) {
    let answer = 0;
    const MOD = 1_000_000_007;
    const board = Array.from({length: N}, () => Array(M).fill(0));
    for (const [x, y] of puddles) {
        board[x-1][y-1] = -1;
    }
    
    board[0][0] = 1;
    const STEPS = [[0, 1], [1, 0]];
    for (let i=0; i<N; ++i) {
        for (let j=0; j<M; ++j) {
            for (let k=0; k<2; ++k) {
                const ni = i+STEPS[k][0];
                const nj = j+STEPS[k][1];
                if (ni>=N || nj >=M || board[i][j] === -1 || board[ni][nj] === -1) continue;
                board[ni][nj] += board[i][j];
                board[ni][nj] %= MOD;
            }
        }
    }
    
    return board[N-1][M-1];
}