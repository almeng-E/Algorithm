function solution(maps) {
    let answer = 0;
    
    const board = maps;
    const N = board.length;
    for (let i=0; i<N; ++i) {
        board[i] = board[i].split('');    
    }
    
    const M = board[0].length;
    let sx = -1;
    let sy = -1;
    for (i=0; i<N; ++i) {
        for (j=0; j<M; ++j) {
            if (board[i][j] === 'S') {
                sx = i;
                sy = j;
            }        
        }
    }
    
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];
    
    // V[x][y][레버여부]
    const V = Array.from({length: N}, () => 
                        Array.from({length: M}, () => 
                                  Array.from({length: 2}, ()=>Infinity)));
    
    
    const Q = [[sx, sy, 0]];
    let qIdx = 0;
    V[sx][sy][0] = 0;
    
    while (Q.length > qIdx) {
        const [x, y, isOpen] = Q[qIdx++];
        
        for (let d=0; d<4; ++d) {
            const nx = x+dx[d];
            const ny = y+dy[d];
            
            if (nx < 0 || nx >= N || ny < 0 || ny >= M ||
                board[nx][ny] === 'X' || V[nx][ny][isOpen] <= V[x][y][isOpen] + 1) continue;
            
            if (board[nx][ny] === 'E' && isOpen === 1) {
                return V[x][y][isOpen] + 1;
            }
            else if (board[nx][ny] === 'L' && isOpen === 0) {
                V[nx][ny][0] = V[x][y][0] + 1;
                if (V[nx][ny][1] > V[nx][ny][0]) {
                    V[nx][ny][1] = V[nx][ny][0];
                    Q.push([nx, ny, 1]);
                }
            }
            else {
                V[nx][ny][isOpen] = V[x][y][isOpen] + 1;
                Q.push([nx, ny, isOpen]);
            }
        }
    }
    
    return -1;
}