function solution(board) {
    let answer = Infinity;
    
    const N = board.length;
    //          상 우 하 좌
    const dx = [-1, 0, 1, 0];
    const dy = [0, 1, 0, -1];
    
    // V[x][y][di]
    const V = Array.from({length: N}, () => 
                        Array.from({length: N}, () => 
                                  Array.from({length: 4}, () => Infinity)))
    
    const Q = [];
    let qIdx = 0
    for (let di=0; di<4; ++di) {
        Q.push([0, 0, di]);
        V[0][0][di] = 0;
    }
    
    while (Q.length > qIdx) {
        const [x, y, di] = Q[qIdx++];
        let [nx, ny, nCost, ndi] = [0,0,0,0];
        for (let dd=0; dd<4; ++dd) {
            if (dd === 2) continue;
            else if (dd === 0) {
                ndi = di;
                nx = x+dx[ndi];
                ny = y+dy[ndi];
                nCost = 100;
            }
            else {
                ndi = (di+dd) % 4;
                nx = x+dx[ndi];
                ny = y+dy[ndi];
                nCost = 600;
            }

            if (nx<0 || nx>=N || ny<0 || ny>=N ||board[nx][ny] === 1 || V[nx][ny][ndi] <= V[x][y][di] + nCost) continue;

            V[nx][ny][ndi] = V[x][y][di] + nCost;
            Q.push([nx, ny, ndi]);
        }
    }
    
    for (let i=0; i<4; ++i) {
        answer = Math.min(answer, V[N-1][N-1][i]);
    }
    
    
    return answer;
}