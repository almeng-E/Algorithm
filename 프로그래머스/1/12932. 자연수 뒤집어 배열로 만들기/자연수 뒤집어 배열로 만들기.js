function solution(n) {
    const answer = String(n).split("").map(x=>Number(x)).reverse();
    
    return answer;
}