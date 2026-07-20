function solution(PN) {
    let answer = '*'.repeat(PN.length-4) + PN.slice(-4);
    
    return answer;
}