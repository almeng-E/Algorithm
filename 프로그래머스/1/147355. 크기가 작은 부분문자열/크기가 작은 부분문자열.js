function solution(t, p) {
    let answer = 0;
    const len = p.length;
    const num = Number(p);

    for (let i=0; i<t.length-len+1; ++i) {
        if (Number(t.slice(i, i+len)) <= num) answer++;
    }
    
    
    return answer;
}