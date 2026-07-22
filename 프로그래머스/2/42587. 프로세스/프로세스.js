function solution(priorities, location) {
    let answer = 0;
    
    const N = priorities.length;
    const order = [...priorities].sort((a, b) => b-a);
    
    let oIdx = 0;
    let pIdx = 0;
    
    const res = [];
    while (oIdx < N) {
        if (priorities[pIdx] === order[oIdx]) {
            oIdx++;
            res.push(pIdx);
        }
        pIdx++;
        pIdx %= N;
    }
    
    for (let i=0; i<N; ++i) {
        if (res[i] === location) {
            answer = i+1;
            break;
        }
    }
    return answer;
}