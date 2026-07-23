function solution(N, M, queries) {
    const answer = [];
    
    const board = Array.from({length: N}, () => 
                            Array.from({length: M}, () => 0));
    let cnt = 1;
    for (let i=0; i<N; ++i) {
        for (let j=0; j<M; ++j) {
            board[i][j] = cnt++;
        }
    }
    
    for (let qi=0; qi<queries.length; ++qi) {
        const x1 = queries[qi][0] -1;
        const y1 = queries[qi][1] -1;
        const x2 = queries[qi][2] -1;
        const y2 = queries[qi][3] -1;
    
        let tmp = board[x1][y1];
        let tmp2 = tmp;
        let ret = tmp;
        for (j=y1+1; j<=y2; ++j) {  
            tmp2 = board[x1][j];
            board[x1][j] = tmp;
            tmp = tmp2;
            ret = Math.min(tmp, ret);
        }
        for (i=x1+1; i<=x2; ++i) {   
            tmp2 = board[i][y2];
            board[i][y2] = tmp;
            tmp = tmp2;
            ret = Math.min(tmp, ret);
        }
        for (j=y2-1; j>=y1; --j) {
            tmp2 = board[x2][j];
            board[x2][j] = tmp;
            tmp = tmp2;
            ret = Math.min(tmp, ret);
        }
        for (i=x2-1; i>=x1; --i) {
            tmp2 = board[i][y1];
            board[i][y1] = tmp;
            tmp = tmp2;
            ret = Math.min(tmp, ret)
        }
        answer.push(ret)
    }
    
    
    return answer;
}