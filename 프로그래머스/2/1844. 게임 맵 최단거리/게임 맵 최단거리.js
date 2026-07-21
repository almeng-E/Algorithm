function solution(maps) {
    let answer = 0;
    const [N, M] = [maps.length, maps[0].length];
    const STEPS = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    
    // bfs
    const Q = [[0, 0]];
    let qIdx = 0;
    const V = Array.from({length: N}, () => 
        Array.from({length: M}, () => Infinity)
    )
    V[0][0] = 1;
    
    while (Q.length > qIdx) {
        const [x, y] = Q[qIdx];
        if ((x === N-1) && (y === M-1)) break;

        qIdx++;
        for (let i=0; i<4; ++i) {
            const dx = STEPS[i][0];
            const dy = STEPS[i][1];
            
            const nx = x+dx;
            const ny = y+dy;
            
            if (nx < 0 || nx >= N || ny < 0 || ny >= M || maps[nx][ny] === 0 || V[nx][ny] <= V[x][y]+1) continue;
            V[nx][ny] = V[x][y] + 1;
            Q.push([nx, ny]);
        }
    }
    return (V[N-1][M-1] === Infinity) ? -1 : V[N-1][M-1];
    
}