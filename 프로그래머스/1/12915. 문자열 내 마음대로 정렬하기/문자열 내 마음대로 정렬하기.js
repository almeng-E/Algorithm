function solution(S, n) {
    const answer = [];
    
    S.sort((a, b) => {
        if (a[n] < b[n]) return -1;
        if (a[n] > b[n]) return 1;

        if (a < b) return -1;
        if (a >= b) return 1;
        
    })
    
    return S;
}