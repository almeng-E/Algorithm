function solution(t, p) {
    let answer = 0;
    
    const N = p.length;
    p = Number(p);
    for (let i=0; i<=t.length-N; ++i) {
        answer += (Number(t.slice(i, i+N)) <= p) ? 1 : 0;
    }
    
    return answer;
}