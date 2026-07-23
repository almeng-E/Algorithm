function solution(players, callings) {
    const answer = [...players];
    
    const dict = new Map();    
    for (i=0; i<players.length; ++i) {
        dict.set(players[i], i);
    }
    
    for (const p1 of callings) {
        const idx1 = dict.get(p1);
        const idx2 = idx1-1;
        const p2 = answer[idx2];
        
        answer[idx1] = p2;
        answer[idx2] = p1;
        
        dict.set(p2, idx1);
        dict.set(p1, idx2);
        
        
    }
    
    
    return answer;
}